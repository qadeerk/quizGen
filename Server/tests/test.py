import os
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.metrics import ContextualRelevancyMetric
from langchain_openai import ChatOpenAI
from getProperty import load_api_key

from promptTemplates.FactTemplates.factExtraction import fact_extraction_template

os.environ['OPENAI_API_KEY'] = load_api_key()

llm = ChatOpenAI(openai_api_key=load_api_key(),
                 model_name="gpt-4o-mini",
                 temperature= 0.0)

metric = ContextualPrecisionMetric(
    threshold=0.7,
    model="gpt-4",
    include_reason=True
)

def test_answer_relevancy():
    answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.5)
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        actual_output=llm.invoke(fact_extraction_template.format(topic="topic")),
        retrieval_context=["All customers are eligible for a 30 day full refund at no extra cost."]
    )
    assert_test(test_case, [answer_relevancy_metric])
    
    
    # deepeval test run test_example.py