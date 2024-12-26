import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deepeval.test_case import LLMTestCase
from deepeval import evaluate
from deepeval.metrics import SummarizationMetric
from langchain_openai import ChatOpenAI
from promptTemplates.FactTemplates.questionGeneration import question_generation_template
from langfuse.callback import CallbackHandler
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

langfuse_handler = CallbackHandler(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST")
)


llm = ChatOpenAI(model_name="gpt-4o-mini",
                 temperature= 0.0)

# This is the summary, replace this with the actual output from your LLM application
actual_output= llm.invoke(question_generation_template.format(text="jon is 5 feet tall"),config={"callbacks": [langfuse_handler]})

print(actual_output.content)
