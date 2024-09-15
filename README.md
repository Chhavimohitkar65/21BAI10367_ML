
## 🌟 QueryMorph

### Document Retrieval System with GPT-3.5-turbo

This project implements a **Document Retrieval System** that integrates GPT-3.5-turbo for query expansion and answer generation. It fetches and ranks documents based on user queries, leveraging MongoDB for document storage, Redis for caching, and web scraping to keep documents updated. The system is designed to provide fast and accurate search results using a combination of modern NLP techniques.

![Simple Presentation in Pink Lilac Pastel Blobs Basic Style](https://github.com/user-attachments/assets/67faf02f-3e0a-4364-a5c7-87606c787e2b)

---

## 🌟 Key Features

### ⚡ FastAPI Setup
- **Endpoints:**
  - `/health`: Verify if the API is running.
  - `/search`: Search for documents based on user queries, expands them using GPT-3.5-turbo, and generates context-based answers from the retrieved documents.

### 📚 Document Storage in MongoDB
- Efficiently stores documents and their embeddings in MongoDB for fast retrieval and ranked search results.

### 🚀 Redis Cache for Performance
- Caches query results using Redis to boost performance for repeated queries. Cache entries expire after one hour, ensuring fresh content.

### 🧠 Query Expansion with GPT-3.5
- Automatically expands user queries using OpenAI's **GPT-3.5-turbo** model, improving the accuracy of document retrieval.

### ✨ Answer Generation with GPT-3.5
- Provides human-like, context-aware answers based on retrieved documents using **GPT-3.5-turbo**, enhancing user interactions.

### 🔍 Advanced Document Similarity Search
- Calculates **cosine similarity** between the query embeddings and document embeddings stored in MongoDB, ranking the results based on similarity scores.

### ⚠️ User Request Limiting
- Each user can make up to **5 search requests**. After that, the system triggers an HTTP `429 - Too Many Requests` error to prevent abuse.

### 📰 Automated News Scraping
- News articles from **BBC**, **CNN**, and **The New York Times** are scraped using **newspaper3k** and stored in MongoDB for enhanced, real-time searchability.

### 🌐 Streamlit Frontend
- A user-friendly **Streamlit** interface allows users to:
  - Input search queries.
  - View expanded queries and similarity scores.
  - Scrape news articles.
  - Check API health.

### 🔄 Background News Scraping
- A background thread automatically scrapes news articles when the FastAPI server starts, keeping the document database updated.

### 🐳 Dockerized for Easy Deployment
- Fully containerized using **Docker** with:
  - Python 3.10-slim base image for efficiency.
  - All dependencies pre-installed via `requirements.txt`.
  - Exposed ports for **Streamlit (8501)**.
  - Runs both FastAPI and Streamlit concurrently in the same container for seamless service.

### ✅ Health Check Endpoint
- The `/health` endpoint ensures the FastAPI service is up and running, providing an operational check.

### 🔄 Concurrent FastAPI & Streamlit Execution
- Both **FastAPI** and **Streamlit** run concurrently using **threading**, making the system accessible from a single Docker container.


## Architecture Diagram And Demonstration video
https://drive.google.com/drive/folders/1L7LG9xm2iWcN8gHYf3tqBO1brAo7lt32?usp=sharing

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
4. Set up your environment variables:
    ```bash
    OPENAI_API_KEY=your_openai_api_key
    MONGO_URI=your_mongodb_uri

    ```
 5. Start MongoDB and Redis services:
    - Ensure MongoDB is running locally or on a remote server.
    - Start Redis using the following command:
    ```bash
    redis-server
    ```

6. Run the FastAPI server
    ```bash
    uvicorn main:app --reload
    ```
    
7. Run the Streamlit app
    ```bash
    streamlit run app.py

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

- recruitments@trademarkia.com
