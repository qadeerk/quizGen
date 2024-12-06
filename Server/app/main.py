import os
import sys
import json
import uuid
from fastapi import FastAPI, HTTPException, Request
from langchain_openai import ChatOpenAI
from fastapi.middleware.cors import CORSMiddleware

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from promptChain.factChain.chain import factBasedQuizGenerationChain
from promptChain.utils.jsonUtils import getCleanJson
from quizDb import SaveQuiz, GetQuiz

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generateQuiz")
async def generate_quiz(request: Request):
    try:
        data = await request.json()
        context = data.get("context")
        job_description = data.get("jobDescription")
        cv_data = data.get("cvData")
        
        
        quiz = getCleanJson(factBasedQuizGenerationChain(context))
        # Generate a UUID
        quiz_id = str(uuid.uuid4())
        SaveQuiz(quiz_id, quiz)

        response = {}
        response["quiz_id"] = quiz_id
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/getQuiz")
async def generate_quiz(id: str):
    print(f"Getting quiz with UUID: {id}")
    return GetQuiz(id)

# Mock APIs below ( These are just for developing the front end )
@app.get("/getMockQuiz")
async def generate_quiz(id: int):
    try:
        print(id)
        return json.dumps([
            {
            "question": {
                "id": 1,
                "value": "What is the capital of France?"
            },
            "options": [
                {"id": 1, "value": "Paris"},
                {"id": 2, "value": "London"},
                {"id": 3, "value": "Berlin"},
                {"id": 4, "value": "Madrid"}
            ],
            "answerIndex": 0
            },
            {
            "question": {
                "id": 2,
                "value": "What is the capital of Germany?"
            },
            "options": [
                {"id": 1, "value": "Paris"},
                {"id": 2, "value": "London"},
                {"id": 3, "value": "Berlin"},
                {"id": 4, "value": "Madrid"}
            ],
            "answerIndex": 2
            },
            {
            "question": {
                "id": 3,
                "value": "What is the capital of Spain?"
            },
            "options": [
                {"id": 1, "value": "Paris"},
                {"id": 2, "value": "London"},
                {"id": 3, "value": "Berlin"},
                {"id": 4, "value": "Madrid"}
            ],
            "answerIndex": 3
            },
            {
            "question": {
                "id": 4,
                "value": "What is the capital of England?"
            },
            "options": [
                {"id": 1, "value": "Paris"},
                {"id": 2, "value": "London"},
                {"id": 3, "value": "Berlin"},
                {"id": 4, "value": "Madrid"}
            ],
            "answerIndex": 1
            }
        ])

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


    try:
        return "submited"

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# TODO : https://www.youtube.com/watch?v=D-JD4tM0NvU (Restructure application)