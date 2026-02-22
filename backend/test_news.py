import requests
from bs4 import BeautifulSoup
import urllib.parse

def test_google_rss_news(query="동계올림픽"):
    print(f"Testing Google News RSS for: {query}")
    try:
        encoded_query = urllib.parse.quote(query)
        url = f"https://news.google.com/rss/search?q={encoded_query}&hl=ko&gl=KR&ceid=KR:ko"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'xml') # XML parser
        
        items = soup.find_all('item')
        if not items:
            print("No results found in RSS.")
            return

        for item in items[:5]:
            title = item.title.text
            link = item.link.text
            pub_date = item.pubDate.text
            print(f"Title: {title}")
            print(f"Date: {pub_date}")
            print(f"Link: {link}")
            print("-" * 20)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_google_rss_news()
