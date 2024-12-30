# LangGraph

LangGraph를 이용한 테스트 프로젝트입니다.
다음 테크포스팅의 내용을 담고 있습니다.
* [LangGrpah] 1. LangGrpah(랭그래프)를 이용한 AI Workflow 관리하기(https://x2bee.tistory.com/429)
* [LangGrpah] 2. LangGrpah(랭그래프)의 핵심 요소의 개념적 이해(https://x2bee.tistory.com/430)
* [LangGrpah] 3. Chain과 Agent를 이용한 Workflow 구현 - 쿼리 추출 모델(https://x2bee.tistory.com/431)
* [LangGrpah] 4. LangGraph를 이용한 RAG 및 검색 Agent 개발(https://x2bee.tistory.com/433)

<div align="center">
  <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F2VMNE%2FbtsKQN8ii20%2FMf29HSEaPy2xCH2BNingw0%2Fimg.png" alt="LangGraph-Workflow" width="600">
  <br></br><b>LangGraph를 이용한 LLM Workflow</b>
</div>

* * *

<div align="center">
  <img src="https://blog.kakaocdn.net/dn/cJtEjX/btsKPAPhg0V/dAIorK5K4l3gGikpXLUXYk/img.gif" alt="Run-Project" width="800">
  <br></br><b>해당 Workflow의 실행예시</b>
</div>

* * *

## Getting started



* 프로젝트 폴더 내부에 api_key폴더 생성
* OpenAI의 API_KEY와 TAVILY_API_KEY를 입력

```
# Example

workspace
├── api_key
│   ├── API_KEY.txt # OpenAI의 API Key가 입력되어있음
│   └── TAVILY_API.txt # Tavily Search의 API Key가 입력되어있음
├── elements
│   ├── __pycache__
│   ├── deges.py
│   ├── nodes.py
│   ├── states.py
│   └── tools.py
├── make_vecterstore.py # chroma_db를 만들 때 사용.
├── run_graph.ipynb # 노트북 형태로 실행
└── run_graph.py
``` 

```
python run_graph.py
```