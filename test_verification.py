import requests
import json
import time

BASE_URL = "http://localhost:5000/api/chat"

test_cases = [
    {"query": "BTS 광화문 공연 뉴스?", "agent": "ReportCreator", "desc": "BTS News as Report"},
    {"query": "현재 배구 트렌드 분석해줘", "agent": "DataAnalyzer", "desc": "Volleyball Trend Analysis"},
    {"query": "Python으로 가위바위보 게임 만들어줘", "agent": "CodeGenerator", "desc": "RPS Game Code"},
    {"query": "오늘 여자배구 경기 일정", "agent": "NewsSearch", "desc": "Volleyball News"},
    {"query": "인공지능의 미래에 대해 조사해줘", "agent": "WebSearch", "desc": "AI Research"},
    {"query": "삼성전자 실적 분석 및 향후 전망", "agent": "DataAnalyzer", "desc": "Samsung Analysis"},
    {"query": "서울 이번주말 축제 리포트 작성해줘", "agent": "ReportCreator", "desc": "Seoul Fest Report"},
    {"query": "Flask 서버 기본 코드 생성", "agent": "CodeGenerator", "desc": "Flask Code"},
    {"query": "현재 환율 정보", "agent": "WebSearch", "desc": "FX Info"},
    {"query": "내일 날씨 뉴스", "agent": "NewsSearch", "desc": "Weather News"}
]

def run_tests():
    print(f"Starting 10-Test Verification Suite (Mode-Aware)...")
    results = []
    for i, test in enumerate(test_cases, 1):
        query = test["query"]
        agent = test["agent"]
        print(f"Test {i}/10: Agent: {agent} | Query: {query}")
        try:
            response = requests.post(BASE_URL, json={
                "message": query, 
                "session_id": f"test_mode_{i}",
                "selected_agent": agent
            }, timeout=90)
            
            if response.status_code == 200:
                data = response.json()
                msg = data.get('message', '')
                print(f"  SUCCESS: Result length: {len(msg)}")
                
                # Check for mode indicators
                if agent == "ReportCreator" and "###" in msg:
                    print("  VERIFIED: Report formatting found.")
                elif agent == "DataAnalyzer" and ("분석" in msg or "인사이트" in msg):
                    print("  VERIFIED: Analysis keywords found.")
                elif agent == "CodeGenerator" and "```" in msg:
                    print("  VERIFIED: Code block found.")
                
                results.append({"query": query, "agent": agent, "status": "PASS", "response": msg[:100] + "..."})
            else:
                print(f"  FAILED: Status {response.status_code}")
                results.append({"query": query, "agent": agent, "status": "FAIL", "error": response.text})
        except Exception as e:
            print(f"  ERROR: {str(e)}")
            results.append({"query": query, "agent": agent, "status": "ERROR", "error": str(e)})
        time.sleep(1)
    
    with open("test_results_modes.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("Verification Suite Complete. Results saved to test_results_modes.json")

if __name__ == "__main__":
    run_tests()
