from enum import Enum
import json
import os

class Dataset_path(Enum):
    # Define your dataset enums here
    QUESTION_GENERATION = "testDataSet/questionGeneration"
    JOB_DESCRIPTION = "testDataSet/JobDescription"
    FACT_GENERATION="testDataSet/factsgeneration"
    
class Dataset_type(Enum):
    # Define your dataset enums here
    QUESTION_GENERATION_SMALL = "small"
    JOB_DESCRIPTION_DEFAULT = "skills"
    FACT_GENERATION_SMALL="oop_small"
    FACT_GENERATION_WITH_HEADING="context_with_heading"
    FACT_GENERATION_WITH_LARGER_CONTEXT="larger_context_examples"
    FACT_GENERATION_WITH_SMALLER_CONTEXT="small_context_example"

def GetJsonFileContent(file_path):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print("File does not exist")
            return json.dumps([])
        
        # Read the file content
        with open(file_path, 'r') as file:
            dataset = json.load(file)
        
        return dataset
    except Exception as e:
        print(f"Error reading dataset file: {e}")
        return ""
    
def GetTxtFileContent(file_path):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print("File does not exist")
            return ""
        
        # Read the file content
        with open(file_path, 'r') as file:
            dataset = file.read()
        
        return dataset
    except Exception as e:
        print(f"Error reading dataset file: {e}")
        return ""
    
def GetFilePath(dataset_path, dataset_name, file_extension="json"):
    # print(f"fetching dataset: {dataset_path}/{dataset_name}")
    # Construct the file path
    dataset_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", dataset_path)
    extention = "" if file_extension is False else f".{file_extension}"
    file_path = os.path.join(dataset_folder, f"{dataset_name}{extention}")
    # print(f"File path: {file_path}")
    return file_path
        
def GetDataset(dataset_path, dataset_name):  
    try:
        return GetJsonFileContent(GetFilePath(dataset_path, dataset_name))
    except Exception as e:
        print(f"Error reading dataset file: {e}")
        return ""
    
def GetHidratedDataset(dataset_path, dataset_name):  
    try:
        dataset_Json = GetDataset(dataset_path, dataset_name)
        # print(dataset_Json)
        input_path = GetFilePath(f"{dataset_path}/base", dataset_Json[0]["fileName"], False)
        print(input_path)
        # dataset_Json["input"] = GetTxtFileContent(input_path)
        for item in dataset_Json:
            input_path = GetFilePath(f"{dataset_path}/base", item["fileName"], False)
            item["input"] = GetTxtFileContent(input_path)
        
        return dataset_Json
    except Exception as e:
        print(f"Error reading dataset file: {e}")
        return ""
    
# print(GetHidratedDataset(Dataset_path.JOB_DESCRIPTION.value, Dataset_type.JOB_DESCRIPTION_DEFAULT.value))