import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# todo get llm list , get input list form question generation , write evaluation 
from promptTemplates.FactTemplates.questionGeneration import question_generation_template
from promptTemplates.FactTemplates.factExtraction import fact_extraction_template
from deepeval.metrics import AnswerRelevancyMetric
from utils.getModelList import getOpenAIModelList
from utils.execution_cost_test import get_execution_cost
from utils.dataset import GetDataset , Dataset_path , Dataset_type
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams


from deepeval.test_case import LLMTestCase
from deepeval import assert_test, evaluate
from deepeval.metrics import JsonCorrectnessMetric
from pydantic import BaseModel

class ExampleSchema(BaseModel):
    Question: str
    Answer: str


def add_to_result(data):
    file_path="result.txt"
    try:
        if not os.path.exists(file_path):
            with open(file_path,'w') as file:
                pass
        with open(file_path, 'a') as file:  
            file.write(data + '\n')
    except Exception as e:
        print(f"An error occurred: {e}")



def test_fact_extraction_with_GEVAL(path,name):
    dataset = GetDataset(path, name)
    llms = getOpenAIModelList()
    add_to_result(f"--------{name}")
    for llm in llms:
        add_to_result(f"--------{llm.model_name}--------")
        for item in dataset:
            response = get_execution_cost(llm, fact_extraction_template.format(text=item["Input"]))
            expected_output_str = "\n".join(item["ExpectedOutput"])  #because the geval expects the expected output to be a string
            test_case = LLMTestCase(input=item["Input"], actual_output=response["output"],expected_output=expected_output_str)
            correctness_metric = GEval(name="Completeness",criteria="Determine whether the actual output contains all the correct facts based on the expected output.",
            evaluation_steps=["Verify that the model has extracted all key facts from the input, regardless of its structure (headings, paragraphs, or brief text)",
                              "Compare the extracted facts with the expected output. Verify alignment in terms of content, order, and completeness",
                              "Each fact should be clear, concise, and free from vagueness or ambiguity",
                              "There should be no additional, misleading, or omitted facts"],
            evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],)
            test_assertion=evaluate(test_cases=[test_case],metrics=[correctness_metric],print_results=False,show_indicator=False,verbose_mode=False,write_cache=False)         
            add_to_result(response['output'])
            add_to_result(response['total_cost'])
            add_to_result(str(test_assertion.test_results[0].success))
        

# test_json_iteration(Dataset_path.FACT_GENERATION.value, Dataset_type.FACT_GENERATION_SMALL.value)


test_fact_extraction_with_GEVAL(Dataset_path.FACT_GENERATION.value, Dataset_type.FACT_GENERATION_WITH_HEADING.value)
