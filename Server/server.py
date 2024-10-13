import json
from fastapi import FastAPI, HTTPException
from getProperty import load_api_key
from langchain import OpenAI
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

app = FastAPI()

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)