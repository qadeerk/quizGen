import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deepeval.test_case import LLMTestCase
from deepeval import evaluate
from deepeval.metrics import SummarizationMetric
from langchain_openai import ChatOpenAI
from getProperty import load_api_key
from promptTemplates.FactTemplates.quizGeneration import quiz_generation_template
from dotenv import load_dotenv


# Load the .env file
load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o",
                 temperature= 0.0)

questionsList = [{'Question': 'What does Object-Oriented Programming (OOP) focus on in software design?', 'Answer': 'OOP focuses on organizing software design around data or objects.'}, {'Question': 'What are the key principles of Object-Oriented Programming (OOP)?', 'Answer': 'Encapsulation, inheritance, polymorphism, and abstraction.'}, {'Question': 'What are the main benefits of encapsulation and inheritance in object-oriented programming?', 'Answer': 'Encapsulation protects data integrity, while inheritance promotes code reuse and extensibility.'}]

first_question = questionsList[1]['Question']
first_answer = questionsList[1]['Answer']

# This is the summary, replace this with the actual output from your LLM application
actual_output= llm.invoke(quiz_generation_template.format(Question=first_question,Answer=first_answer)).content

print(actual_output)

# test_case = LLMTestCase(input=input, actual_output=actual_output)
# metric = SummarizationMetric(
#     threshold=0.5,
#     model="gpt-4",
#     assessment_questions=[
#         "Is the coverage score based on a percentage of 'yes' answers?",
#         "Does the score ensure the summary's accuracy with the source?",
#         "Does a higher score mean a more comprehensive summary?"
#     ]
# )

# evaluate([test_case], [metric])