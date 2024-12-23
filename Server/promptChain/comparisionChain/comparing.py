import os
import sys

# Add the directory two levels above to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import re
from langgraph.graph import Graph
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import RunnableParallel
import json

from promptTemplates.matchingTemplates.matchingOverLappingData import overlaping_data_template
from promptTemplates.matchingTemplates.matchingOverLappingData import non_overlaping_job_description_template

from utils.executionUtils import parallelExecution
from utils.jsonUtils import getCleanJson
from utils.jsonUtils import merge_questions_and_answers

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load the .env file
load_dotenv()

model = ChatOpenAI(model_name="gpt-4o-mini",
                 temperature= 0.0)

def questionGenerationFromFact(index,job_description,cv_data):
    return json.loads(model.invoke(question_generation_template.format(text=fact)).content)

def questionGenerationFromFact(index,job_description,cv_data):
    return json.loads(model.invoke(question_generation_template.format(text=fact)).content)

def outputNode(index,props):
    return getCleanJson(model.invoke(quiz_generation_template.format(Question=props["Question"],Answer=props["Answer"])).content)

# def factExtractionNode(input):
#     return json.loads(model.invoke(fact_extraction_template.format(text=input)).content)

# def questionGenerationNode(factList):
#     results = parallelExecution(factList, questionGenerationFromFact)
#     return list(results.values())

# def quizGenerationNode(questionsAndAnswerList):
#     results = parallelExecution(questionsAndAnswerList, quizGenerationFromQuestionAndAnswer)
#     return merge_questions_and_answers(questionsAndAnswerList,list(results.values()))

workflow = Graph()

workflow.add_node("factExtraction", factExtractionNode)
workflow.add_node("questionGeneration", questionGenerationNode)
workflow.add_node("quizGeneration", quizGenerationNode)

workflow.add_edge("factExtraction", "questionGeneration")
workflow.add_edge("questionGeneration", "quizGeneration")

workflow.set_entry_point("factExtraction")
workflow.set_finish_point("quizGeneration")

app = workflow.compile()
    
def factBasedQuizGenerationChain(text):
    response = app.invoke(text)
    return response


# oopText = """Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. These objects represent entities with defined properties and behaviors, encapsulating data and methods that operate on the data within a single unit. This encapsulation fosters modularity, making it easier to manage complexity in large systems by breaking them down into smaller, self-contained units. The design emphasizes abstraction, enabling developers to focus on high-level functionality without delving into implementation details, promoting clarity and reusability in software development.
# Central to OOP are principles that govern its structure and methodology. These principles include encapsulation, inheritance, polymorphism, and abstraction. Encapsulation involves bundling data and methods within an object, restricting access to certain components to safeguard the integrity of the system. Inheritance allows for the creation of new entities that inherit characteristics from existing ones, promoting code reuse and extensibility. Polymorphism enables entities to take on multiple forms, allowing for flexible and dynamic interactions in the program. Together, these principles create a robust framework for designing software that is maintainable, scalable, and aligned with real-world problem-solving approaches."""

# s3text = """Amazon S3 (Simple Storage Service) is a cloud-based object storage solution offered by Amazon Web Services (AWS), designed to store and retrieve any amount of data at any time, from anywhere on the web. It is highly scalable, durable, and cost-effective, making it suitable for a wide range of use cases, including backup and recovery, data archiving, application hosting, and big data analytics. S3 operates on a pay-as-you-go model, allowing businesses to manage storage costs efficiently without upfront investments. It provides eleven nines (99.999999999%) of durability by replicating data across multiple geographically dispersed facilities, ensuring that your data remains safe and accessible even in the event of hardware failures or outages.
# One of the key features of S3 is its support for a variety of storage classes tailored to different use cases and cost considerations. For instance, S3 Standard is ideal for frequently accessed data, while S3 Glacier and S3 Glacier Deep Archive are designed for long-term data archiving at lower costs. Additionally, S3 offers advanced features like versioning, lifecycle policies, and event notifications, enabling seamless data management and integration with other AWS services. Its robust security measures include encryption in transit and at rest, fine-grained access controls, and compliance with various regulatory standards. With its high performance, flexibility, and ease of integration, Amazon S3 is a cornerstone for organizations looking to leverage cloud storage for their modern data needs."""

# print(factBasedQuizGenerationChain(s3text))

# for output in workflow.compile().stream(s3text):
#     # stream() yields dictionaries with output keyed by node name
#     for key, value in output.items():
#         print(f"Output from node '{key}':")
#         print("---")
#         print(value)
#     print("\n---\n")