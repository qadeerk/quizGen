
import json
import os
import sys
from typing import List

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# todo get llm list , get input list form question generation , write evaluation 
from promptTemplates.JobDescriptionDataTemplates.dataExtraction import skill_Extraction_template
from utils.getModelList import getOpenAIModelList
from utils.execution_cost_test import get_execution_cost
from utils.dataset import GetDataset , GetHidratedDataset, Dataset_path , Dataset_type
from utils.compareOutput import JsonSimilarityScoreMetric
from utils.jsonUtils import parse_json_markdown

from deepeval.test_case import LLMTestCase
from deepeval import  evaluate
from deepeval.metrics import JsonCorrectnessMetric
from pydantic import BaseModel, RootModel
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

class Skills(BaseModel):
    category: str
    skills: List[str]
    
class SkillsList(RootModel[List[Skills]]):
    pass

def test_jobDescription(llms,dataset,schema):
    for llm in llms:
        for item in dataset:
            response = get_execution_cost(llm, skill_Extraction_template.format(jobDescription=item["input"]))
            actual_output = parse_json_markdown(response["output"])
            print(actual_output)
            # responce output is markdown json 
            test_case = LLMTestCase(input=item["input"], actual_output=json.dumps(actual_output), expected_output=json.dumps(item["expectedOutput"]))
            JsonCorrectness_metric = JsonCorrectnessMetric(expected_schema=schema,include_reason=False,verbose_mode=False)
            JsonSimilarityScore_metric = JsonSimilarityScoreMetric(include_reason=False,async_mode=False)
            test_assertion = evaluate(test_cases=[test_case],metrics=[JsonCorrectness_metric,JsonSimilarityScore_metric],print_results=False,show_indicator=False,verbose_mode=False,write_cache=False)
            print("------------------")
            print(llm.model_name)
            print(response["output"])
            print(response['total_cost'])
            print(f"test results : {test_assertion.test_results}")
            # print(f"Was test sucessfull : {test_assertion.test_results[0].success}")
            print("------------------")

dataset = GetHidratedDataset(Dataset_path.JOB_DESCRIPTION.value, Dataset_type.JOB_DESCRIPTION_DEFAULT.value)
llms = getOpenAIModelList()

# print(dataset)
test_jobDescription(llms,dataset,SkillsList)