import json
from fastapi import FastAPI, HTTPException
from getProperty import load_api_key
from langchain import OpenAI
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from fastapi.middleware.cors import CORSMiddleware

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

# Initialize OpenAI with your API key
openai_api_key = load_api_key()  # Replace with your OpenAI API key
# llm = OpenAI(api_key=openai_api_key)
llm = ChatOpenAI(openai_api_key=openai_api_key,
                 model_name="gpt-4o-mini")

@app.get("/generateQuiz")
async def generate_quiz(topic: str):
    try:
        # Define your prompt for generating a quiz
        prompt_template = PromptTemplate.from_template("Generate a quiz with 4 numbered questions about {topic}.")

        prompt_input = prompt_template.format(topic=topic)

        # Generate the quiz
        response = llm.invoke(prompt_input)

        return {"quiz": response.content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




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

@app.get("/submitMockQuizResponce")
async def generate_quiz():
    try:
        return "submited"

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



# TODO : https://www.youtube.com/watch?v=D-JD4tM0NvU (Restructure application)