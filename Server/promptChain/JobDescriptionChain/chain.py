import os
import sys

# Add the directory two levels above to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from langgraph.graph import Graph
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import json

from promptTemplates.FactTemplates.contextextractionSimilarSkills import context_extraction_template
from promptTemplates.JobDescriptionDataTemplates.dataExtraction import skill_Extraction_template
from promptChain.factChain.chain import factBasedQuizGenerationChain

from utils.executionUtils import parallelExecution
from utils.jsonUtils import getCleanJson
from utils.jsonUtils import parse_json_markdown
from utils.getLangfuseConfig import getLangChainConfig
from langgraph.types import StreamWriter
from typing import AsyncGenerator

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load the .env file
load_dotenv()

model = ChatOpenAI(model_name="gpt-4o-mini",temperature=0.0)
model4o = ChatOpenAI(model_name="gpt-4o",temperature=0.0)

def generateSkillSetFromJobDescriptionNode(input, writer: StreamWriter):
    try:
        if(writer):
            writer({"event": "Generating skill set from job description"})
        skillSet = {}
        response = model.invoke(skill_Extraction_template.format(jobDescription=input))
        # skillSet = parse_json_markdown('```json\n[\n    {\n        "category": "Tools",\n        "skills": [\n            "JIRA",\n            "Git",\n            "Gitlab",\n            "BitBucket"\n        ]\n    },\n    {\n        "category": "Frameworks",\n        "skills": [\n            "Angular",\n            "Vue",\n            "React",\n            "Material Design",\n            "Bootstrap",\n            "Foundation"\n        ]\n    },\n    {\n        "category": "Technologies",\n        "skills": [\n            "JavaScript",\n            "HTML",\n            "CSS"\n        ]\n    },\n    {\n        "category": "Interpersonal/Transferable Skills",\n        "skills": [\n            "Problem-solving",\n            "Troubleshooting",\n            "Verbal communication",\n            "Written communication",\n            "Collaboration",\n            "Teamwork"\n        ]\n    },\n    {\n        "category": "Managerial Skills",\n        "skills": [\n            "Agile development methodologies",\n            "Scrum"\n        ]\n    }\n]\n```')
        skillSet = parse_json_markdown(response.content)
    except (json.JSONDecodeError, Exception) as e:
        print(f"Error generating skill set: {e}")
        skillSet = {}
    # print(skillSet)
    return skillSet

def _contextGenerationFromSkillCategory(index, skillCategory):
    try:
        # print(str(skillCategory['skills']))
        response = model4o.invoke(context_extraction_template.format(skillset=skillCategory['skills']))
        context_data = response.content
    except (json.JSONDecodeError, Exception) as e:
        print(f"Error generating context: {e}")
        context_data = {}
    return {
        "category": skillCategory['category'],
        "skills": skillCategory['skills'],
        "context": context_data}

def generateContextFromSkillSetNode(skillList, writer: StreamWriter):
    if(writer):
        writer({"event": "Generating context from skill set"})
    try:
        skillsWithContext = list(parallelExecution(skillList, _contextGenerationFromSkillCategory).values())
    except Exception as e:
        print(f"Error generating context from skill set: {e}")
        skillsWithContext = []
    # print(skillsWithContext)
    return skillsWithContext

def _sectionGenerationFromSkillContext(index, skillContexts):
    response = factBasedQuizGenerationChain(skillContexts['context'])
    
    result = {
        "title": str(skillContexts['category']),
        "description": "In this section the questions will be releated to: " + ", ".join(skillContexts["skills"]),
        "questions": getCleanJson(response)}
    # print("----------------------")
    # print(result)
    return result

def generateQuizSectionFromContextNode(skillsWithContextList, writer: StreamWriter):
    if(writer):
        writer({"event": "Generating quiz section from context"})
    try:
        sections = parallelExecution(skillsWithContextList, _sectionGenerationFromSkillContext)
    except Exception as e:
        print(f"Error generating quiz section from context: {e}")
        sections = []
    print(sections)
    sections = list(sections.values())
    writer({
            "event": "final",
            "quiz": {
                "id": "uuid",
                "name": "Sample Quiz 1",
                "description": 'This is a sample quiz description.',
                "instructions": 'Please read the instructions carefully before starting the quiz.',
                "sections": sections
            }
        })
    return sections

workflow = Graph()

workflow.add_node("generateSkillSetFromJobDescription", generateSkillSetFromJobDescriptionNode)
workflow.add_node("generateContextFromSkillSet", generateContextFromSkillSetNode)
workflow.add_node("generateQuizSectionFromContextNode", generateQuizSectionFromContextNode)

workflow.add_edge("generateSkillSetFromJobDescription", "generateContextFromSkillSet")
workflow.add_edge("generateContextFromSkillSet", "generateQuizSectionFromContextNode")

workflow.set_entry_point("generateSkillSetFromJobDescription")
workflow.set_finish_point("generateQuizSectionFromContextNode")

app = workflow.compile()

def generateQuizFromJobDescription(jd):
    sections = app.invoke(input=jd)
    return {
        "id": "uuid",
        "name": 'Sample Quiz 1',
        "description": 'This is a sample quiz description.',
        "instructions": 'Please read the instructions carefully before starting the quiz.',
        "sections": sections
    }

async def generateQuizFromJobDescriptionStream(jd) -> AsyncGenerator:
    async for chunk in app.astream(input=jd, stream_mode="custom"):
        json_Chunk = json.dumps(chunk, sort_keys=True)
        yield json_Chunk
