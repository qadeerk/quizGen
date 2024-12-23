from enum import Enum
import json
import os

class Dataset_path(Enum):
    # Define your dataset enums here
    QUESTION_GENERATION = "testDataSet/questionGeneration"
    
    
    
class Dataset_type(Enum):
    # Define your dataset enums here
    QUESTION_GENERATION_SMALL = "small"


def GetDataset(dataset_path, dataset_name):  
    try:
        # print(f"fetching dataser: {dataset_path}{dataset_name}")
        # Construct the file path
        dataset_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", dataset_path)
        file_path = os.path.join(dataset_folder, f"{dataset_name}.json")
        # print(f"File path: {file_path}")
        
        # Check if the file exists
        if not os.path.exists(file_path):
            print("File does not exist")
            return json.dumps([])
        
        # Read the file content
        with open(file_path, 'r') as file:
            dataset = json.load(file)
        
        return dataset
    except Exception as e:
        print(f"Error reading quiz file: {e}")
        return ""