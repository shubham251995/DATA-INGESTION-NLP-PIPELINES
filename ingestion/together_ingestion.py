import requests
from bs4 import BeautifulSoup

class TogetherIngestion:
    def __init__(self, discussion_id):
        self.base_url = "https://together.bunq.com/api/discussions/"
        self.discussion_id = discussion_id

    def fetch_data(self):
        """Fetch data from Together API."""
        url = f"{self.base_url}{self.discussion_id}"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Failed to fetch data for {self.discussion_id}. Status Code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching data from Together API: {e}")
            return None

    def clean_html(self, html_content):
        """Function to remove HTML tags and return plain text."""
        soup = BeautifulSoup(html_content, "html.parser")
        return soup.get_text()  # Extract plain text from HTML content
    
    def process_data(self, data):
        """Process the fetched data for NLP."""
        if not data:
            return None
        
        content_html = data.get('included', [{}])[0].get('attributes', {}).get('contentHtml', 'No content available')
        return self.clean_html(content_html)
