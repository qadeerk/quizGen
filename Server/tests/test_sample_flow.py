import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# todo get llm list , get input list form question generation , write evaluation 
from promptTemplates.FactTemplates.questionGeneration import question_generation_template
from utils.getModelList import getOpenAIModelList
from utils.execution_cost_test import get_execution_cost
from utils.dataset import GetDataset , Dataset_path , Dataset_type

from deepeval.test_case import LLMTestCase
from deepeval import assert_test, evaluate
from deepeval.metrics import JsonCorrectnessMetric
from pydantic import BaseModel

class ExampleSchema(BaseModel):
    Question: str
    Answer: str

def test_json_iteration():
    small = GetDataset(Dataset_path.QUESTION_GENERATION.value, Dataset_type.QUESTION_GENERATION_SMALL.value)
    llms = getOpenAIModelList()
    for llm in llms:
        for item in small:
            response = get_execution_cost(llm, question_generation_template.format(text=item["Input"]))
            test_case = LLMTestCase(input=item["Input"], actual_output=response["output"])
            JsonCorrectness_metric = JsonCorrectnessMetric(expected_schema=ExampleSchema,include_reason=False,verbose_mode=False)
            test_assertion = evaluate(test_cases=[test_case],metrics=[JsonCorrectness_metric],print_results=False,show_indicator=False,verbose_mode=False,write_cache=False)
            print("------------------")
            print(llm.model_name)
            print(response["output"])
            print(response['total_cost'])
            print(test_assertion.test_results[0].success)
            print("------------------")
        
test_json_iteration()