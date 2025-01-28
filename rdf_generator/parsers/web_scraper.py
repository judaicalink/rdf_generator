import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, url, headers=None):
        """
        Initialize the WebScraper with a target URL.
        """
        self.url = url
        self.headers = headers or {"User-Agent": "Mozilla/5.0"}

    def fetch_content(self):
        """
        Fetches the HTML content of the web page.
        """
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching content from {self.url}: {e}")

    def extract_data(self, css_selector):
        """
        Extracts data from the web page based on the provided CSS selector.
        Returns a list of extracted values.
        """
        try:
            html_content = self.fetch_content()
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.select(css_selector)
            return [element.get_text(strip=True) for element in elements]
        except Exception as e:
            raise Exception(f"Error extracting data: {e}")

    def extract_links(self, css_selector="a"):
        """
        Extracts all links (href attributes) from elements matching the CSS selector.
        """
        try:
            html_content = self.fetch_content()
            soup = BeautifulSoup(html_content, "html.parser")
            elements = soup.select(css_selector)
            return [element.get("href") for element in elements if element.get("href")]
        except Exception as e:
            raise Exception(f"Error extracting links: {e}")
