from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from dotenv import load_dotenv
import os
load_dotenv()





# AnswerRelevancy Metrics

def getAnswerRelevancyScore(input,actual_output):
    metric = AnswerRelevancyMetric(
    threshold=0.7,
    model="gpt-4o",
    include_reason=True
)
    test_case = LLMTestCase(
    input=input,
    # Replace this with the actual output from your LLM application
    actual_output=actual_output
)
    metric.measure(test_case)
    return metric.score