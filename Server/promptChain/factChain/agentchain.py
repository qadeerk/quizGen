import os
import sys
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.tools import tool

from utils.executionUtils import parallelExecution
from utils.jsonUtils import getCleanJson
from utils.jsonUtils import merge_questions_and_answers


from promptTemplates.FactTemplates.factExtraction import fact_extraction_template
from promptTemplates.FactTemplates.questionGeneration import question_generation_template
from promptTemplates.FactTemplates.quizGeneration import quiz_generation_template

# Load environment variables
load_dotenv()

# Initialize the language model
model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.0)

# Define helper functions
@tool("fact_extraction")
def fact_extraction_tool(input: str) -> dict:
    result = json.loads(model.invoke(fact_extraction_template.format(text=input)).content)
    print("Fact Extraction Tool Result:", result)
    return result

@tool("question_generation")
def question_generation_tool(fact_list: list) -> list:
    def question_generation_task(index, fact):
        return json.loads(model.invoke(question_generation_template.format(text=fact)).content)

    results = parallelExecution(fact_list, question_generation_task)
    return list(results.values())

@tool("quiz_generation")
def quiz_generation_tool(questions_and_answers: list) -> list:
    def quiz_generation_task(index, props):
        return getCleanJson(
            model.invoke(
                quiz_generation_template.format(Question=props["Question"], Answer=props["Answer"])
            ).content
        )
    
    results = parallelExecution(questions_and_answers, quiz_generation_task)
    return merge_questions_and_answers(questions_and_answers, list(results.values()))


tools = [
    Tool(
        name="Fact Extraction",
        func=fact_extraction_tool,
        description="Extracts facts from a given text."
    ),
    Tool(
        name="Question Generation",
        func=question_generation_tool,
        description="Generates questions from extracted facts."
    ),
    Tool(
        name="Quiz Generation",
        func=quiz_generation_tool,
        description="Generates quizzes based on questions and answers."
    ),
]

agent = initialize_agent(tools, model, agent_type="zero-shot-react-description")

# Fact-based quiz generation function
def fact_based_quiz_generation_chain(text: str) -> dict:
    response = agent.run(f"""
        1. Extract facts from the input text.
        2. Generate questions based on those facts.
        3. Generate a quiz from the questions and their answers.
        Input: {text}
    """)
    return response

# Example input text
input_text = """Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. These objects represent entities with defined properties and behaviors, encapsulating data and methods that operate on the data within a single unit. This encapsulation fosters modularity, making it easier to manage complexity in large systems by breaking them down into smaller, self-contained units. The design emphasizes abstraction, enabling developers to focus on high-level functionality without delving into implementation details, promoting clarity and reusability in software development.
Central to OOP are principles that govern its structure and methodology. These principles include encapsulation, inheritance, polymorphism, and abstraction. Encapsulation involves bundling data and methods within an object, restricting access to certain components to safeguard the integrity of the system. Inheritance allows for the creation of new entities that inherit characteristics from existing ones, promoting code reuse and extensibility. Polymorphism enables entities to take on multiple forms, allowing for flexible and dynamic interactions in the program. Together, these principles create a robust framework for designing software that is maintainable, scalable, and aligned with real-world problem-solving approaches.."""
print(fact_based_quiz_generation_chain(input_text))
