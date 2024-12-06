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


How to Run

Set Up Virtual Environment:
python3 -m venv myeve
source myeve/bin/activate  # Activate the virtual environment
Install Dependencies:
pip install -r requirements.txt
Run the Project:
python main.py
Provide Input:
When prompted, enter discussion IDs (comma-separated) to fetch data and analyze feedback.
Example: 59881, 24142, 50011
Output:
Sentiment analysis results for each discussion.
Topic modeling insights for grouped discussions.
Visualizations: Word clouds and sentiment distribution plots.
Results

Sentiment Analysis:
Classified feedback as Positive, Negative, or Neutral.
Example: Discussion 59881: Positive
Topic Modeling:
Identified key discussion themes such as payment issues, feature requests, and new product offerings.
LLM Router Integration:
Summarized user feedback into concise insights for actionable decisions.
Future Enhancements

Implement real-time streaming for continuous data ingestion.
Integrate additional data sources, such as Google Drive and GitLab.
Use advanced NLP models (e.g., BERT, DistilBERT) for better accuracy in sentiment analysis and topic modeling.
Containerize the project using Docker for scalable deployment.
