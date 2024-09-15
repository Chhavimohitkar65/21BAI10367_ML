# Document Retrieval System with GPT-3.5-turbo

This project implements a **Document Retrieval System** that integrates GPT-3.5-turbo for query expansion and answer generation. It fetches and ranks documents based on user queries, leveraging MongoDB for document storage, Redis for caching, and web scraping to keep documents updated. The system is designed to provide fast and accurate search results using a combination of modern NLP techniques.

![Simple Presentation in Pink Lilac Pastel Blobs Basic Style](https://github.com/user-attachments/assets/67faf02f-3e0a-4364-a5c7-87606c787e2b)

---

## Features
**FastAPI Setup**
A FastAPI server is implemented to handle API requests, with two endpoints:
/health: Health check endpoint to verify if the API is running.
/search: Searches for documents based on user query, applies GPT-3.5-turbo for query expansion, and generates an answer based on retrieved documents.
2. **Document Storage in MongoDB**
Documents and their corresponding embeddings are stored in MongoDB for efficient retrieval.
3. **Redis Cache for Results**
Redis is used to cache query results to improve performance for repeat queries. Cached results expire after one hour.
4. **Query Expansion Using GPT-3.5**
Queries are expanded and enhanced using OpenAI's GPT-3.5-turbo model to improve document retrieval accuracy.
5. **Answer Generation Using GPT-3.5**
Answers to user queries are generated using the context of the retrieved documents, leveraging GPT-3.5-turbo.
6.**Document Similarity Search**
Cosine similarity is calculated between the user's query embedding and the document embeddings stored in MongoDB. Results are ranked and returned based on similarity scores.
7. **User Request Limiting**
Each user is allowed a maximum of 5 search requests. After that, an HTTP 429 error ("Too Many Requests") is triggered to prevent abuse.
8.**News Scraping**
News articles from sources like BBC, CNN, and The New York Times are scraped using newspaper3k and stored in MongoDB. The content is also embedded for similarity searches.
9. **Streamlit Frontend**
A Streamlit interface allows users to:
Input queries and search documents.
View expanded queries and similarity scores.
Scrape news articles.
Check API health.
10. **Background Thread for Scraping**
News scraping is done automatically in the background as soon as the FastAPI server starts, ensuring up-to-date information.
11. **Dockerization**
The application is containerized using Docker, with the following features:
Python 3.10-slim image for efficiency.
All dependencies installed via requirements.txt.
Ports exposed for Streamlit (8501).
Easy deployment of both FastAPI and Streamlit in the same container.
12. **Health Check Endpoint**
A /health endpoint is available to check the status of the FastAPI service, ensuring the backend is operational.
13. **Concurrent FastAPI and Streamlit**
FastAPI and Streamlit run concurrently using threading, ensuring both services are accessible simultaneously within the Docker container.
---

## Architecture Diagram

![Architecture Diagram](./architecture_diagram.png)

### System Components:

1. **Frontend (UI)**: Built with Streamlit to offer a user-friendly interface for inputting queries and viewing results.
2. **MongoDB**: Stores document data, including content and embeddings, for efficient search and retrieval.
3. **Redis**: A caching layer that stores search results temporarily to speed up future queries.
4. **OpenAI GPT-3.5-turbo**: Expands user queries and generates answers based on the retrieved documents.
5. **Document Ranking**: Combines cosine similarity (via embeddings) and TF-IDF to rank documents.
6. **Web Scraper**: Periodically scrapes and updates articles from news websites, storing them in MongoDB.

---

## Technologies Used

- **Streamlit**: Provides the user interface.
- **MongoDB**: A NoSQL database to store and retrieve documents.
- **Redis**: Caching service to store search results temporarily.
- **OpenAI GPT-3.5-turbo**: Expands user queries and generates natural language answers.
- **Sentence Transformers**: Used for generating document and query embeddings.
- **scikit-learn**: Utilized for TF-IDF computation and cosine similarity calculation.
- **newspaper3k** & **BeautifulSoup**: For scraping and parsing HTML content from news websites.

---

## Prerequisites

- Python 3.8 or above
- MongoDB (for document storage)
- Redis (for caching)
- OpenAI API Key

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/21BAI10367_ML.git
    ```

2. Navigate to the project directory:
    ```bash
    cd 21BAI10367_ML
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

### 1. Search for Documents:
- Input a query in the Streamlit app.
- GPT-3.5-turbo expands the query and retrieves relevant documents from MongoDB.
- Documents are ranked based on cosine similarity and TF-IDF scores.

### 2. Scrape News Articles:
- The web scraper fetches the latest news articles from various sources and stores them in MongoDB.
- Click the "Scrape News" button in the UI to trigger scraping manually.

### 3. Cached Results:
- Search results are cached in Redis to speed up repeated queries within a set time frame.

---

## Query Flow Overview

1. **User Query**: Input query through the Streamlit UI.
2. **Query Expansion**: GPT-3.5-turbo expands the query for more comprehensive results.
3. **Document Retrieval**: Documents are fetched from MongoDB and ranked using embeddings and TF-IDF.
4. **Re-ranking and Answer Generation**: Refined results are presented, and an answer is generated using GPT-3.5-turbo.
5. **Results Display**: Final results are shown in the UI, and the response is cached for future queries.

---

## Future Enhancements

- **PDF and Word Document Support**: Extend to support formats like PDF and Word documents.
- **Summarization**: Add document summarization for quick insights.
- **Authentication**: Implement user authentication for personalized document retrieval.
- **Scalability**: Optimize the system for larger datasets and more concurrent users.

---

## Contributors

- [Your Name](mailto:recruitments@trademarkia.com)
