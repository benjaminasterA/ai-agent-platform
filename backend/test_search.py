from duckduckgo_search import DDGS
import logging

logging.basicConfig(level=logging.DEBUG)

def test_search():
    print("Testing DDGS search...")
    try:
        with DDGS() as ddgs:
            results = ddgs.text("2026 Olympics", max_results=3)
            for r in results:
                print(f"Found: {r.get('title')}")
    except Exception as e:
        print(f"FAILED: {e}")

if __name__ == "__main__":
    test_search()
