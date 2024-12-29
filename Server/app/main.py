import json
import os
import shutil
import sys
import uuid
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from langchain_openai import ChatOpenAI
import pymupdf4llm

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from promptChain.factChain.chain import factBasedQuizGenerationChain
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

@app.post("/generateQuiz")
async def generate_quiz(request: Request):
    try:
        data = await request.json()
        context = data.get("context")
        job_description = data.get("jobDescription")
        cv_data = data.get("cvData")
        
        
        quiz = getCleanJson(factBasedQuizGenerationChain(context))
        # # Generate a UUID
        quiz_id = str(uuid.uuid4())
        SaveQuiz(quiz_id, quiz)

        response = {}
        response["quiz_id"] = quiz_id
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generateQuiz/v2")
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

@app.get("/getQuiz")
async def generate_quiz(id: str):
    return GetQuiz(id)

    
# @app.route("/process", methods=["POST"])
# def ats():
#     doc = request.files['pdf_doc']
#     doc.save(os.path.join(UPLOAD_PATH, "file.pdf"))
#     doc_path = os.path.join(UPLOAD_PATH, "file.pdf")
#     data = _read_file_from_path(doc_path)
#     data = ats_extractor(data)

#     return render_template('index.html', data = json.loads(data))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# TODO : https://www.youtube.com/watch?v=D-JD4tM0NvU (Restructure application)