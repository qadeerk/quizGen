
import json
import os


def SaveQuiz(quiz_uuid:str, data):
    print(f"Saving quiz with UUID: {quiz_uuid}")
    print(f"Data: {data}")
    # Create the Quizes folder if it doesn't exist
    quizes_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Quizes")
    os.makedirs(quizes_folder, exist_ok=True)

    # Define the file path
    file_path = os.path.join(quizes_folder, f"{quiz_uuid}.json")
    print(f"File path: {file_path}")
    
    # Write the response to the file, overriding any existing content
    with open(file_path, "w") as f:
        json.dump(data, f)

def GetQuiz(quiz_uuid:str):  
    try:
        print(f"Getting quiz with UUID: {quiz_uuid}")
        # Construct the file path
        quizes_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Quizes")
        file_path = os.path.join(quizes_folder, f"{quiz_uuid}.json")
        print(f"File path: {file_path}")
        
        # Check if the file exists
        if not os.path.exists(file_path):
            print("File does not exist")
            return ""
        
        # Read the file content
        with open(file_path, 'r') as file:
            quiz_data = json.load(file)
        
        return quiz_data
    except Exception as e:
        print(f"Error reading quiz file: {e}")
        return ""

def SubmitQuiz(quiz_uuid, data):
    return True

def getAllQuizes(quiz_uuid, data):
    return True

def getAllSubmissionsForAQuiz(quiz_uuid, data):
    return True

# SaveQuiz("234", {"quiz": "dataasdsa"})
# print(GetQuiz("123"))