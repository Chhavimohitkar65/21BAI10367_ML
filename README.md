# Document Retrieval System with GPT-3.5-turbo

This project implements a **Document Retrieval System** that integrates GPT-3.5-turbo for query expansion and answer generation. It fetches and ranks documents based on user queries, leveraging MongoDB for document storage, Redis for caching, and web scraping to keep documents updated. The system is designed to provide fast and accurate search results using a combination of modern NLP techniques.

![Simple Presentation in Pink Lilac Pastel Blobs Basic Style](https://github.com/user-attachments/assets/67faf02f-3e0a-4364-a5c7-87606c787e2b)

---

## Features

- **Document Search**: Retrieves and ranks documents stored in MongoDB based on query similarity using embeddings and cosine similarity.
- **Query Expansion**: GPT-3.5-turbo expands user queries to improve search accuracy.
- **Re-ranking with TF-IDF**: Refines search results using cosine similarity combined with TF-IDF scores for improved ranking.
- **Caching with Redis**: Caches search results to improve response time and reduce database load.
- **News Scraping**: Automatically scrapes articles from sources like BBC, CNN, and NY Times, periodically updating the document database.
- **Answer Generation**: Generates natural language answers from retrieved documents using GPT-3.5-turbo.

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
