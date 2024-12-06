from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import numpy as np

class TopicModeling:
    def __init__(self, num_topics=3):
        """Initialize the topic modeling class."""
        self.num_topics = num_topics

    def perform_topic_modeling(self, documents):
        """Perform topic modeling using Latent Dirichlet Allocation (LDA)."""
        # Step 1: Convert the text data into a TF-IDF matrix
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(documents)

        # Step 2: Apply LDA for topic modeling
        lda = LatentDirichletAllocation(n_components=self.num_topics, random_state=42)
        lda.fit(X)

        # Step 3: Display the top words in each topic
        feature_names = np.array(vectorizer.get_feature_names_out())
        topics = []
        for topic_idx, topic in enumerate(lda.components_):
            topics.append(" ".join([feature_names[i] for i in topic.argsort()[:-10 - 1:-1]]))  # Top 10 words per topic
        
        return topics
