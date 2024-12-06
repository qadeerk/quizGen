import re
import json
import random

def getCleanJson(dirty_json):
    if dirty_json.startswith("```json"):
        # Remove the first 7 characters and the last 3 characters
        cleaned_json = dirty_json[7:-3]
    else:
        cleaned_json = dirty_json
    
    # Remove any \n or other escape characters
    cleaned_json = re.sub(r'\\[nrt]', '', cleaned_json)
    
    return json.loads(cleaned_json)
    
# Example usage
dirtyJson = '```json\n{\n    "option1": ["OOP focuses on organizing software design around functions and procedures."],\n    "option2": ["OOP emphasizes the use of global variables in programming."],\n    "option3": ["OOP is primarily concerned with optimizing code for performance."]\n}\n```'
# print(getCleanJson(dirtyJson)) 


def mergeJsonObjects(questions, answers):
    try:
        if not isinstance(questions, list) or not isinstance(answers, list):
            raise ValueError("Both inputs must be lists")
        
        if len(questions) != len(answers):
            raise ValueError("The number of questions and answers must be the same")
        
        merged_list = []
        for question, answer in zip(questions, answers):
            merged_list.append({"question": question, "answer": answer})
        
        return merged_list
    except ValueError as e:
        print(f"Value error: {e}")
        return None

# Example usage
questions = ["What is the capital of France?", "What is 2 + 2?"]
answers = ["Paris", "4"]
# print(mergeJsonObjects(questions, answers))


def merge_questions_and_answers(correct_answers, false_answers) -> json:
    merged_data = []
    
    # Iterate over both lists simultaneously
    for index, (correct, false) in enumerate(zip(correct_answers, false_answers)):
        question = correct['Question']
        correct_answer = correct['Answer']
        
        # Collect all answers
        all_answers = [correct_answer] + list(false.values())
        
        # Randomize the order of answers
        randomized_answers = random.sample(all_answers, len(all_answers))
        
        # Find the index of the correct answer in the randomized list
        correct_index = randomized_answers.index(correct_answer)
        
        # Create the merged object
        merged_data.append({
            "question": {"id": index,"value": question},
            "options": [{"id": idx, "value": answer} for idx, answer in enumerate(randomized_answers)],
            "answerIndex": correct_index
        })
    
    return json.dumps(merged_data, indent=4)


# Data from the two nodes
correct_answers = [
    {'Question': 'What does Object-Oriented Programming (OOP) focus on in software design?', 'Answer': 'OOP focuses on organizing software design around data or objects.'},
    {'Question': 'What are the key principles of Object-Oriented Programming (OOP)?', 'Answer': 'Encapsulation, inheritance, polymorphism, and abstraction.'},
    {'Question': 'What are the main benefits of encapsulation and inheritance in object-oriented programming?', 'Answer': 'Encapsulation protects data integrity, while inheritance promotes code reuse and extensibility.'}
]

false_answers = [
    {'1': 'OOP focuses on organizing software design around functions and procedures.', '2': 'OOP emphasizes the use of global variables in programming.', '3': 'OOP is primarily concerned with optimizing code for performance.'},
    {'1': 'Modularity, concurrency, data flow, and recursion', '2': 'Procedural programming, functional programming, logic programming, and event-driven programming', '3': 'Static typing, dynamic typing, strong typing, and weak typing'},
    {'1': 'Encapsulation allows for faster execution, while inheritance reduces memory usage.', '2': 'Encapsulation simplifies user interfaces, while inheritance eliminates the need for polymorphism.', '3': 'Encapsulation enhances security, while inheritance restricts code flexibility.'}
]

# Generate the merged JSON
# merged_json = merge_questions_and_answers(correct_answers, false_answers)
# print(merged_json)