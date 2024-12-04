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

from promptTemplates.FactTemplates.factExtraction import fact_extraction_template
from promptTemplates.FactTemplates.questionGeneration import question_generation_template
from promptTemplates.FactTemplates.quizGeneration import quiz_generation_template

from promptChain.utils.executionUtils import parallelExecution
from promptChain.utils.jsonUtils import getCleanJson
from promptChain.utils.jsonUtils import merge_questions_and_answers

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load the .env file
load_dotenv()

model = ChatOpenAI(model_name="gpt-4o-mini",
                 temperature= 0.0)

def questionGenerationFromFact(index,fact):
    return json.loads(model.invoke(question_generation_template.format(text=fact)).content)

def quizGenerationFromQuestionAndAnswer(index,props):
    return getCleanJson(model.invoke(quiz_generation_template.format(Question=props["Question"],Answer=props["Answer"])).content)

def factExtractionNode(input):
    return json.loads(model.invoke(fact_extraction_template.format(text=input)).content)

def questionGenerationNode(factList):
    results = parallelExecution(factList, questionGenerationFromFact)
    return list(results.values())

def quizGenerationNode(questionsAndAnswerList):
    results = parallelExecution(questionsAndAnswerList, quizGenerationFromQuestionAndAnswer)
    return merge_questions_and_answers(questionsAndAnswerList,list(results.values()))

workflow = Graph()

workflow.add_node("factExtraction", factExtractionNode)
workflow.add_node("questionGeneration", questionGenerationNode)
workflow.add_node("quizGeneration", quizGenerationNode)

workflow.add_edge("factExtraction", "questionGeneration")
workflow.add_edge("questionGeneration", "quizGeneration")

workflow.set_entry_point("factExtraction")
workflow.set_finish_point("quizGeneration")

app = workflow.compile()

text = """Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. These objects represent entities with defined properties and behaviors, encapsulating data and methods that operate on the data within a single unit. This encapsulation fosters modularity, making it easier to manage complexity in large systems by breaking them down into smaller, self-contained units. The design emphasizes abstraction, enabling developers to focus on high-level functionality without delving into implementation details, promoting clarity and reusability in software development.
Central to OOP are principles that govern its structure and methodology. These principles include encapsulation, inheritance, polymorphism, and abstraction. Encapsulation involves bundling data and methods within an object, restricting access to certain components to safeguard the integrity of the system. Inheritance allows for the creation of new entities that inherit characteristics from existing ones, promoting code reuse and extensibility. Polymorphism enables entities to take on multiple forms, allowing for flexible and dynamic interactions in the program. Together, these principles create a robust framework for designing software that is maintainable, scalable, and aligned with real-world problem-solving approaches."""

print(app.invoke(text))

# for output in app.stream(text):
#     # stream() yields dictionaries with output keyed by node name
#     for key, value in output.items():
#         print(f"Output from node '{key}':")
#         print("---")
#         print(value)
#     print("\n---\n")