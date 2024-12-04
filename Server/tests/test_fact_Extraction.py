import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deepeval.test_case import LLMTestCase
from deepeval import evaluate
from deepeval.metrics import SummarizationMetric
from langchain_openai import ChatOpenAI
from getProperty import load_api_key
from promptTemplates.FactTemplates.factExtraction import fact_extraction_template
from dotenv import load_dotenv


# Load the .env file
load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o-mini",
                 temperature= 0.0)


# This is the original text to be summarized
input = """
The 'coverage score' is calculated as the percentage of assessment questions
for which both the summary and the original document provide a 'yes' answer. This
method ensures that the summary not only includes key information from the original
text but also accurately represents it. A higher coverage score indicates a
more comprehensive and faithful summary, signifying that the summary effectively
encapsulates the crucial points and details from the original content.
"""

# This is the summary, replace this with the actual output from your LLM application
actual_output= llm.invoke(fact_extraction_template.format(text=input)).content

print(actual_output)

test_case = LLMTestCase(input=input, actual_output=actual_output)
metric = SummarizationMetric(
    threshold=0.5,
    model="gpt-4",
    assessment_questions=[
        "Is the coverage score based on a percentage of 'yes' answers?",
        "Does the score ensure the summary's accuracy with the source?",
        "Does a higher score mean a more comprehensive summary?"
    ]
)

evaluate([test_case], [metric])