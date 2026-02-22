import requests
from bs4 import BeautifulSoup

def test_naver_search(query="동계올림픽"):
    print(f"Testing Naver News search for: {query}")
    try:
        url = f"https://search.naver.com/search.naver?where=news&query={query}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Referer': 'https://www.naver.com/'
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Naver Search News 결과의 다양한 클래스들 시도
        articles = soup.find_all('a', class_=['news_tit', 'news_a', 'api_txt_lines'])
        if not articles:
            # 보조 셀렉터 시도
            articles = soup.select('ul.list_news li div.news_area a.news_tit')
        
        if not articles:
            print("Trying discovery mode (href containing 'news.naver.com'):")
            articles = [a for a in soup.find_all('a', href=True) if 'news.naver.com' in a.get('href') and len(a.get_text()) > 5]
        
        if not articles:
            print("Still no results. Listing first 50 links with href:")
            for a in soup.find_all('a', href=True)[:50]:
                print(f"Text: {a.get_text()[:30]} | Href: {a.get('href')[:50]}")
            return

        for a in articles[:3]:
            print(f"Title: {a.get_text()}")
            print(f"Link: {a.get('href')}")
            print("-" * 20)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_naver_search()
