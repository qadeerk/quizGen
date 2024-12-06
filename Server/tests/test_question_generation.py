import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deepeval.test_case import LLMTestCase
from deepeval import evaluate
from deepeval.metrics import SummarizationMetric
from langchain_openai import ChatOpenAI
from getProperty import load_api_key
from promptTemplates.FactTemplates.questionGeneration import question_generation_template
from dotenv import load_dotenv


# Load the .env file
load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o-mini",
                 temperature= 0.0)

# This is the summary, replace this with the actual output from your LLM application
actual_output= llm.invoke(question_generation_template.format(text="jon is 5 feet tall")).content

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