import streamlit as st
import openai
import os
import time
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import redis
from newspaper import Article
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import threading
from dotenv import load_dotenv

# Set up FastAPI app
app = FastAPI()

# Load environment variables from .env file
load_dotenv()
# Access the variables
openai.api_key = os.getenv("OPENAI_API_KEY")
client = MongoClient(os.getenv("MONGO_URI"))

db = client['document_retrieval']
documents_collection = db['documents']
users_collection = db['users']

# Redis setup for caching
redis_cache = redis.StrictRedis(host='localhost', port=6379, db=0)

# Load sentence-transformers model for embeddings
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# GPT-3.5-turbo API call for Query Expansion
def gpt_expand_query(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Please rephrase or expand the following query: {query}"}
        ]
    )
    return response['choices'][0]['message']['content']

# GPT-3.5-turbo API call for Answer Generation
def gpt_generate_answer(query, documents):
    context = " ".join([doc['content'] for doc in documents])
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that uses context to answer questions."},
            {"role": "user", "content": f"Here is the context: {context}. Now, answer the question: {query}"}
        ]
    )
    return response['choices'][0]['message']['content']

# Cache the results using Redis
def cache_results(user_id, query, results):
    redis_cache.set(f"{user_id}:{query}", str(results), ex=3600)

# Check if the results are cached
def check_cache(user_id, query):
    cached = redis_cache.get(f"{user_id}:{query}")
    return cached if cached else None

# Increment user request count
def increment_user_request(user_id):
    user = users_collection.find_one({"user_id": user_id})
    if user:
        if user["request_count"] >= 5:
            st.error("HTTP 429: Too Many Requests")
            return False
        else:
            users_collection.update_one({"user_id": user_id}, {"$inc": {"request_count": 1}})
            return True
    else:
        users_collection.insert_one({"user_id": user_id, "request_count": 1})
        return True

# Document search based on cosine similarity
def search_documents(query, top_k=5, threshold=0.5):
    query_embedding = model.encode([query])
    
    # Fetch all documents and their embeddings from MongoDB
    docs = list(documents_collection.find())
    doc_embeddings = [doc['embedding'] for doc in docs]
    
    # Calculate similarity scores
    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]
    top_matches = [(docs[i], similarities[i]) for i in range(len(similarities)) if similarities[i] >= threshold]
    
    # Sort and limit results
    top_matches = sorted(top_matches, key=lambda x: x[1], reverse=True)[:top_k]
    return [match[0] for match in top_matches], top_matches

# News Scraping Logic
def scrape_news():
    news_sources = [
        "https://www.bbc.com/news",
        "https://www.cnn.com/world",
        "https://www.nytimes.com/section/world",
    ]
    
    scraped_articles = []
    
    for source in news_sources:
        response = requests.get(source)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find article links (customize based on site structure)
        for link in soup.find_all('a', href=True):
            article_url = link['href']
            
            if article_url.startswith("http"):  # Ignore internal URLs
                try:
                    # Use newspaper3k to extract the article content
                    article = Article(article_url)
                    article.download()
                    article.parse()
                    
                    # Save article to MongoDB if it's valid
                    if article.text:
                        article_data = {
                            'title': article.title,
                            'content': article.text,
                            'url': article_url,
                            'embedding': model.encode([article.text])[0].tolist()
                        }
                        documents_collection.insert_one(article_data)
                        scraped_articles.append(article_data)
                        
                        st.write(f"Scraped: {article.title}")
                except Exception as e:
                    st.write(f"Error scraping {article_url}: {str(e)}")
    
    st.write(f"Scraped {len(scraped_articles)} articles from the sources.")
    return scraped_articles


@app.on_event("startup")
def startup_event():
    # Start scraping in a background thread as soon as the server starts
    threading.Thread(target=scrape_news, daemon=True).start()

# Streamlit App
st.title("QueryMorph")

user_id = st.text_input("Enter User ID")
query = st.text_input("Enter search query")
top_k = st.number_input("Top K results", value=5, min_value=1)
threshold = st.slider("Similarity Threshold", 0.0, 1.0, 0.5)

# Button to scrape news
if st.button("Scrape News"):
    scrape_news()

# Button to search documents
if st.button("Search"):
    if increment_user_request(user_id):
        cached_results = check_cache(user_id, query)
        
        if cached_results:
            st.write(f"Cached Results for '{query}':")
            st.write(cached_results)
        else:
            expanded_query = gpt_expand_query(query)
            st.write(f"Expanded Query: {expanded_query}")
            results, similarities = search_documents(expanded_query, top_k, threshold)
            cache_results(user_id, query, results)
            st.write(f"Results for '{expanded_query}':")
            for doc, similarity in zip(results, similarities):
                st.write(f"Document: {doc['content']}, Similarity: {similarity[1]:.2f}")
            answer = gpt_generate_answer(query, results)
            st.write(f"Generated Answer: {answer}")

# Button to check health of the FastAPI service
if st.button("Check API Health"):
    try:
        health_response = requests.get("http://localhost:8000/health")
        if health_response.status_code == 200:
            st.success(f"API Health: {health_response.json()}")
        else:
            st.error(f"API Health Check Failed: Status {health_response.status_code}")
    except Exception as e:
        st.error(f"Error checking API health: {str(e)}")


# FastAPI API Endpoints

# Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "API is healthy"}

# Define a Pydantic model for /search request
class SearchRequest(BaseModel):
    user_id: str
    query: str
    top_k: int = 5
    threshold: float = 0.5

# Search Endpoint
@app.post("/search")
def search_documents_api(request: SearchRequest):
    if increment_user_request(request.user_id):
        expanded_query = gpt_expand_query(request.query)
        results, _ = search_documents(expanded_query, request.top_k, request.threshold)
        answer = gpt_generate_answer(request.query, results)
        return {"results": results, "answer": answer}
    else:
        return {"error": "HTTP 429: Too Many Requests"}

# Run FastAPI in a separate thread
def run_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Run FastAPI in the background
threading.Thread(target=run_fastapi, daemon=True).start()

