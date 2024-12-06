class ProcessTogetherData:
    def __init__(self, data):
        self.data = data

    def extract_content(self):
        """Extract and clean content from the fetched data."""
        content_html = self.data.get('included', [{}])[0].get('attributes', {}).get('contentHtml', 'No content available')
        return self.clean_html(content_html)

    def clean_html(self, html_content):
        """Function to remove HTML tags and return plain text."""
        soup = BeautifulSoup(html_content, "html.parser")
        return soup.get_text()  # Extract plain text from HTML content
