
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# todo get llm list , get input list form question generation , write evaluation 
from promptTemplates.FactTemplates.questionGeneration import question_generation_template
from utils.getModelList import getOpenAIModelList
# from utils.execution_cost_test import get_execution_cost
from utils.dataset import GetDataset , Dataset_path , Dataset_type
from utils.compareOutput import similarityScoreMetric

from deepeval.test_case import LLMTestCase
from deepeval import  evaluate
from deepeval.metrics import JsonCorrectnessMetric
from pydantic import BaseModel


def test_jobDescription(llms,dataset,schema):
    for llm in llms:
        for item in dataset:
            # response = get_execution_cost(llm, question_generation_template.format(text=item["Input"]))
            # test_case = LLMTestCase(input=item["Input"], actual_output=response["output"], expected_output=response["output"])
            test_case = LLMTestCase(input=str(item["input"]), actual_output=str(item["actualOutput"]), expected_output=str(item["expectedOutput"]))
            JsonCorrectness_metric = JsonCorrectnessMetric(expected_schema=schema,include_reason=False,verbose_mode=False)
            similarityScore_metric = similarityScoreMetric(include_reason=False)
            test_assertion = evaluate(test_cases=[test_case],metrics=[similarityScore_metric],print_results=False,show_indicator=False,verbose_mode=False,write_cache=False)
            print("------------------")
            print(llm.model_name)
            # print(response["output"])
            # print(response['total_cost'])
            print(test_assertion.test_results)
            print("------------------")
            

dataset = GetDataset(Dataset_path.JOB_DESCRIPTION.value, Dataset_type.JOB_DESCRIPTION_DEFAULT.value)
llms = getOpenAIModelList()
class JobSchema(BaseModel):
    jobTitle: str
        
test_jobDescription(llms,dataset,JobSchema)