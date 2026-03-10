import requests
import json

tests = [
    {
        "name": "TEST 1 - Simple Clean Python",
        "payload": {
            "code": "def add(a, b):\n    return a + b\n"
        }
    },
    {
        "name": "TEST 2 - Problematic Python",
        "payload": {
            "code": "import os\n\ndef calculate(data):\n    total = 0\n    for i in data:\n        for j in data:\n            total += i * j\n    eval(\"print('hello')\")\n    return total\n"
        }
    },
    {
        "name": "TEST 3 - Clean JavaScript",
        "payload": {
            "code": "function sum(a, b) {\n  return a + b;\n}\n"
        }
    },
    {
        "name": "TEST 4 - Bad JavaScript",
        "payload": {
            "code": "function compute(data) {\n    var result = 0;\n    for (var i = 0; i < data.length; i++) {\n        for (var j = 0; j < data.length; j++) {\n            result += data[i] * data[j];\n        }\n    }\n    eval(\"console.log('hello')\");\n    return result;\n}\n"
        }
    },
    {
        "name": "BONUS TEST - Invalid Code",
        "payload": {
            "code": "def broken(:\n  return 5"
        }
    }
]

def run_tests():
    for test in tests:
        print(f"\n{'='*50}")
        print(f"Running {test['name']}")
        print(f"{'='*50}")
        try:
            response = requests.post("http://127.0.0.1:8000/analyze", json=test["payload"])
            print(f"Status Code: {response.status_code}")
            
            data = response.json()
            # print summarized information for easy reading
            print(f"Language: {data.get('language')}")
            print(f"Score: {data.get('score')}")
            print(f"Static Issues count: {len(data.get('static_issues', []))}")
            for issue in data.get('static_issues', []):
                print(f"  - [{issue.get('severity')}] {issue.get('type')}: {issue.get('message')}")
                
            print(f"AI Issues count: {len(data.get('ai_issues', []))}")
            for issue in data.get('ai_issues', []):
                print(f"  - [{issue.get('severity')}] {issue.get('type')}: {issue.get('message')}")

            print(f"LLM Status: {data.get('llm_status')}")
            print(f"Summary: {data.get('summary')}")
            
        except Exception as e:
            print(f"Request failed: {e}")

if __name__ == "__main__":
    run_tests()
