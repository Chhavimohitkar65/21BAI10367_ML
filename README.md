# 21BAI10367_ML
![Simple Presentation in Pink Lilac Pastel Blobs Basic Style](https://github.com/user-attachments/assets/67faf02f-3e0a-4364-a5c7-87606c787e2b)

# Document Retrieval System with GPT-3.5-turbo

This project implements a **Document Retrieval System** that integrates GPT-3.5-turbo for query expansion and answer generation. It fetches and ranks documents based on user queries, leveraging MongoDB for document storage, Redis for caching, and web scraping to keep documents updated. The system aims to provide fast and accurate search results using a combination of modern NLP techniques.

## Features

- **Document Search**: Retrieves and ranks documents stored in MongoDB based on similarity to user queries using embeddings and cosine similarity.
- **Query Expansion**: Uses GPT-3.5-turbo to expand user queries for better search accuracy.
- **Re-ranking with TF-IDF**: Refines search results by re-ranking documents based on cosine similarity combined with TF-IDF scores.
- **Caching with Redis**: Caches search results to improve response time and reduce database load.
- **News Scraping**: Automatically scrapes articles from news sources such as BBC, CNN, and NY Times, periodically updating the document database.
- **Answer Generation**: Leverages GPT-3.5-turbo to generate natural language answers from retrieved documents.

## Architecture Diagram

![Architecture Diagram](./architecture_diagram.png)

### Components:

1. **Frontend (UI)**: Built with Streamlit for a user-friendly interface allowing users to input queries and view results.
2. **MongoDB**: Stores document data including content and embeddings for efficient search and retrieval.
3. **Redis**: Caching layer to store search results temporarily for faster subsequent searches.
4. **OpenAI GPT-3.5-turbo**: Used for expanding user queries and generating natural language answers based on the documents retrieved.
5. **Document Ranking**: Combines cosine similarity (via embeddings) and TF-IDF to rank the retrieved documents.
6. **Web Scraper**: Periodically scrapes and updates articles from news websites, storing them in the MongoDB database.

## Technologies Used

- **Streamlit**: For building the user interface.
- **MongoDB**: NoSQL database to store and retrieve documents.
- **Redis**: Caching service to store search results temporarily.
- **OpenAI GPT-3.5-turbo**: For query expansion and answer generation.
- **Sentence Transformers**: For generating document and query embeddings.
- **scikit-learn**: For TF-IDF computation and cosine similarity.
- **newspaper3k**: For scraping news articles.
- **BeautifulSoup**: For parsing and scraping HTML content from news websites.

## Installation

### Prerequisites

- Python 3.8 or above
- MongoDB
- Redis
- OpenAI API Key

### Steps to Install
To get started with Document Retrieval System, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/21BAI10367_ML.git

2. Navigate to the project directory:
    ```bash
   cd 21BAI10367_ML

3. Install the required dependencies:
    ```bash
   pip install -r requirements.txt

## Usage
