# Data Ingestion and NLP Pipeline

This project is a comprehensive **data ingestion and NLP pipeline** designed to process real-time user feedback from multiple sources, such as the **Together API**, and provide actionable insights through **sentiment analysis**, **topic modeling**, and integration with **LLM models**.

---

## **Key Features**
- **Real-Time Data Ingestion**:
  - Fetch user discussions and feedback from the Together API.
  - Prepare the data for further processing with NLP models.
- **NLP Processing**:
  - Perform **sentiment analysis** to classify user feedback (Positive, Negative, Neutral).
  - Use **topic modeling** to identify recurring themes in discussions.
  - Generate concise summaries using the **LLM Router API**.
- **Visualization**:
  - Generate **word clouds** and **sentiment distribution plots** for intuitive insights.

---

## **Folder Structure**
```plaintext
DATA-INGESTION-NLP-PIPELINE/
├── ingestion/
│   ├── together_ingestion.py      # Script for fetching data from Together API
│   ├── google_drive_ingestion.py  # Placeholder for Google Drive ingestion
├── models/
│   ├── ilm_router.py              # Integration with LLM Router (OpenAI API)
├── NLP/
│   ├── sentiment_analysis.py      # Sentiment analysis implementation
│   ├── topic_modeling.py          # Topic modeling using LDA
├── transformation/
│   ├── process_together_data.py   # Data transformation logic
├── tests/
│   ├── test_ilm_router.py         # Test cases for LLM Router
│   ├── test_together_ingestion.py # Test cases for Together API ingestion
├── main.py                        # Entry point for the project
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
