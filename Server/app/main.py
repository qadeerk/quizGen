import json
import os
import shutil
import sys
import uuid
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse
from langchain_openai import ChatOpenAI
import pymupdf4llm

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from promptChain.factChain.chain import factBasedQuizGenerationChain
from promptChain.JobDescriptionChain.chain import generateQuizFromJobDescription
from promptChain.JobDescriptionChain.chain import generateQuizFromJobDescriptionStream
from utils.jsonUtils import getCleanJson
from utils.jsonUtils import getCleanMarkDownTable
from quizDb import SaveQuiz, GetQuiz

from promptTemplates.matchingTemplates.matchingOverLappingData import overlaping_data_template
from promptTemplates.matchingTemplates.matchingOverLappingData import non_overlaping_job_description_template

app = FastAPI()

# Load the .env file
load_dotenv()

model = ChatOpenAI(model_name="gpt-4o-mini",
                 temperature= 0.0)


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

@app.post("/generateQuiz/jobdescription")
async def generate_quiz_from_Job_Description(jobDescription: str = Form(...)):
    try:
        quiz_id = str(uuid.uuid4())

        quiz = generateQuizFromJobDescription(jd=jobDescription)
        # Generate a UUID
        SaveQuiz(quiz_id, quiz)

        response = {}
        response["quiz_id"] = quiz_id
        return JSONResponse(content={"quizId": quiz_id,})
    
    except ValueError as ve:
        print(f"ValueError: {ve}")
        raise HTTPException(status_code=400, detail="Invalid input provided.")
    except KeyError as ke:
        print(f"KeyError: {ke}")
        raise HTTPException(status_code=400, detail="Missing required data.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
    
@app.post("/generateQuiz/jobdescription/v2")
async def generate_quiz_from_Job_Description_v2(jobDescription: str = Form(...)):
    try:
        quiz_id = str(uuid.uuid4())

        async def event_generator():
            yield json.dumps({'event': 'processing started', 'quiz_id': quiz_id})
            async for data in generateQuizFromJobDescriptionStream(jobDescription):
                try:
                    data_json = json.loads(data)
                    if data_json.get('event') == 'final':
                        print("saving final quiz")
                        SaveQuiz(quiz_id, data_json.get('quiz'))
                    else:
                        yield data
                except json.JSONDecodeError as e:
                    print(f"JSONDecodeError: {e}")
                    yield data
            yield json.dumps({'event': 'processing finished'})

        return StreamingResponse(event_generator(), media_type="text/event-stream")
    
    except ValueError as ve:
        print(f"ValueError: {ve}")
        raise HTTPException(status_code=400, detail="Invalid input provided.")
    except KeyError as ke:
        print(f"KeyError: {ke}")
        raise HTTPException(status_code=400, detail="Missing required data.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
        
@app.post("/generateQuiz")
async def generate_quiz(
    context: str = Form(...),
    jobDescription: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        quiz_id = str(uuid.uuid4())
        
        if file is not None:
            # Save the uploaded file
            file_name = f"{quiz_id}.pdf"
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "uploads", file_name)
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        
        cvDataMd = pymupdf4llm.to_markdown(file_path)
        SaveQuiz(quiz_id, cvDataMd, "md")
        quiz = getCleanJson(factBasedQuizGenerationChain(context))
        # Generate a UUID
        SaveQuiz(quiz_id, quiz)
        
        matchingAtrubuted = getCleanMarkDownTable(model.invoke(overlaping_data_template.format(jobDescription=jobDescription,cvData=cvDataMd)).content)
        nonMatchingAtrubuted = getCleanMarkDownTable(model.invoke(non_overlaping_job_description_template.format(jobDescription=jobDescription,cvData=cvDataMd)).content)

        response = {}
        response["quiz_id"] = quiz_id
        return JSONResponse(
        content={
            "message": "Data and file uploaded successfully",
            "quizId": quiz_id,
            "matchingAtrubuted": matchingAtrubuted,
            "nonMatchingAtrubuted": nonMatchingAtrubuted,
            "filename": file.filename,
        }
    )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/generateQuiz/context")
async def generate_quiz_from_context(
    context: str = Form(...),
    jobDescription: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        quiz_id = str(uuid.uuid4())
        
        if file is not None:
            # Save the uploaded file
            file_name = f"{quiz_id}.pdf"
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "uploads", file_name)
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
        
        cvDataMd = pymupdf4llm.to_markdown(file_path)
        SaveQuiz(quiz_id, cvDataMd, "md")
        quiz = getCleanJson(factBasedQuizGenerationChain(context))
        # Generate a UUID
        SaveQuiz(quiz_id, quiz)
        
        matchingAtrubuted = getCleanMarkDownTable(model.invoke(overlaping_data_template.format(jobDescription=jobDescription,cvData=cvDataMd)).content)
        nonMatchingAtrubuted = getCleanMarkDownTable(model.invoke(non_overlaping_job_description_template.format(jobDescription=jobDescription,cvData=cvDataMd)).content)

        response = {}
        response["quiz_id"] = quiz_id
        return JSONResponse(
        content={"quizId": quiz_id}
    )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/getQuiz")
async def get_quiz(id: str):
    return GetQuiz(id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# TODO : https://www.youtube.com/watch?v=D-JD4tM0NvU (Restructure application)