from ingestion.together_ingestion import TogetherIngestion
from models.llm_router import IlmRouter
from NLP.sentiment_analysis import SentimentAnalysis
from NLP.topic_modeling import TopicModeling
from transformation.process_together_data import ProcessTogetherData

def main():
    # Get user input for discussion IDs
    discussion_ids_input = input("Enter user discussion IDs (comma-separated): ")
    discussion_ids = discussion_ids_input.split(",")  # Convert input string into a list of IDs
    
    all_processed_data = []
    sentiments = []  # To store the sentiment of each discussion
    
    print("\nFetching and processing discussions...\n")
    
    # Loop over the discussion IDs to fetch, process, and prepare data
    for discussion_id in discussion_ids:
        # Ingestion
        ingestion = TogetherIngestion(discussion_id.strip())
        raw_data = ingestion.fetch_data()
        
        if not raw_data:
            continue
        
        # Transformation
        transformer = ProcessTogetherData(raw_data)
        processed_data = transformer.extract_content()
        if not processed_data:
            continue
        
        all_processed_data.append(processed_data)
        
        # Sentiment Analysis
        sentiment_analysis = SentimentAnalysis()
        sentiment = sentiment_analysis.analyze_sentiment(processed_data)
        sentiments.append(sentiment)
    
    if not all_processed_data:
        print("No valid data to process. Exiting.")
        return
    
    # Prepare the message for the LLM Router
    ilm_router = IlmRouter(api_key="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", name_gsd="shubhambhatt_gsd")
    message = [{"role": "system", "content": "Summarize the following content:"}, {"role": "user", "content": " ".join(all_processed_data)}]
    
    llm_response = ilm_router.call_router(message)
    if llm_response:
        print("\nLLM Router Response:\n")
        print(llm_response['response'])
    
    # Perform Topic Modeling on the aggregated LLM response
    topic_modeling = TopicModeling(num_topics=3)
    topics = topic_modeling.perform_topic_modeling(all_processed_data)
    print("\nIdentified Topics:\n")
    for idx, topic in enumerate(topics):
        print(f"Topic #{idx}: {topic}")
    
    # Plot sentiment distribution
    print("\nSentiment Analysis Results:\n")
    plot_sentiment_distribution(sentiments)

    # Generate word cloud based on the sentiment of each discussion
    print("\nGenerating word clouds based on sentiment...\n")
    for idx, sentiment in enumerate(sentiments):
        print(f"Sentiment for discussion {discussion_ids[idx].strip()}: {sentiment}")
        generate_wordcloud(all_processed_data[idx], sentiment_type=sentiment)

def plot_sentiment_distribution(sentiment_list):
    """Plot the distribution of sentiments."""
    sentiment_counts = {'Positive': sentiment_list.count('Positive'), 
                        'Negative': sentiment_list.count('Negative'),
                        'Neutral': sentiment_list.count('Neutral')}
    
    sns.barplot(x=list(sentiment_counts.keys()), y=list(sentiment_counts.values()))
    plt.title("Sentiment Distribution")
    plt.ylabel("Number of Mentions")
    plt.show()

if __name__ == "__main__":
    main()
