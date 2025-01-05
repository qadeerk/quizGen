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

def getCleanMarkDownTable(dirty_markdown):
    
    if dirty_markdown.startswith("```markdown"):
        # Remove the first 7 characters and the last 3 characters
        cleaned_markdown = dirty_markdown[11:-3]
    else:
        cleaned_markdown = dirty_markdown
        
    # Remove any newline escape characters
    cleaned_markdown.replace('\n', '')
    
    return cleaned_markdown
    
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

def parse_json_markdown(json_string: str) -> dict:
    # Remove the triple backticks if present
    json_string = json_string.strip()
    # json_string = re.sub(r'\\[nrt]', '', json_string)
    start_index = json_string.find("```json")
    end_index = json_string.find("```", start_index + len("```json"))

    if start_index != -1 and end_index != -1:
        extracted_content = json_string[start_index + len("```json"):end_index].strip()
        # extracted_content = re.sub(r'\\[nrt]', '', extracted_content)
        # Parse the JSON string into a Python dictionary
        parsed = json.loads(extracted_content)
    elif start_index != -1 and end_index == -1 and json_string.endswith("``"):
        end_index = json_string.find("``", start_index + len("```json"))
        extracted_content = json_string[start_index + len("```json"):end_index].strip()
        
        # Parse the JSON string into a Python dictionary
        parsed = json.loads(extracted_content)
    elif json_string.startswith("{") or json_string.startswith("["):
        # Parse the JSON string into a Python dictionary
        parsed = json.loads(json_string)
    else:
        print(json_string)
        raise Exception("Could not find JSON block in the output.")

    return parsed


markdownJson = '```json\n[\n    {\n        "category": "Tools",\n        "skills": [\n            "JIRA",\n            "Git",\n            "Gitlab",\n            "BitBucket"\n        ]\n    },\n    {\n        "category": "Frameworks",\n        "skills": [\n            "Angular",\n            "Vue",\n            "React",\n            "Material Design",\n            "Bootstrap",\n            "Foundation"\n        ]\n    },\n    {\n        "category": "Technologies",\n        "skills": [\n            "JavaScript",\n            "HTML",\n            "CSS"\n        ]\n    },\n    {\n        "category": "Interpersonal/Transferable Skills",\n        "skills": [\n            "Problem-solving",\n            "Troubleshooting",\n            "Verbal communication",\n            "Written communication",\n            "Collaboration",\n            "Teamwork"\n        ]\n    },\n    {\n        "category": "Managerial Skills",\n        "skills": [\n            "Agile development methodologies",\n            "Scrum"\n        ]\n    }\n]\n```'
# print(parse_json_markdown(markdownJson))
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

markdown= """```markdown\n| Job Requirement                                                                 | Matched Experience in CV                                                                                     |\n|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|\n| Write clean, maintainable, and scalable code in HTML, CSS, and JavaScript.     | Proficient in JavaScript, HTML, and CSS. Developed various applications and modules at Apple and Shopee.     |\n| Use design tools like Adobe Creative Suite (Photoshop, Illustrator, XD) or Figma. | Established UI/UX guidelines and design systems; experience with design tools not explicitly mentioned.        |\n| Build and maintain responsive designs that function on all devices and browsers. | Developed responsive applications and modules, including PWA applications at Snapp.                          |\n| Work closely with UI/UX designers to implement design mockups into functional interfaces. | Collaborated with stakeholders and established design guidelines for UI/UX at Apple.                         |\n| Optimize applications for performance, speed, and scalability.                  | Created performance tracking tools and optimized website loading times at Shopee.                             |\n| Ensure websites and applications adhere to SEO best practices.                  | Experience in optimizing applications, though specific SEO practices not mentioned.                          |\n| Conduct usability testing and ensure cross-browser compatibility.               | Conducted usability testing and ensured cross-browser compatibility in various projects.                      |\n| Debug and fix code issues to maintain seamless user experiences.                | Debugged and fixed code issues in multiple applications developed at Apple and Shopee.                       |\n| Keep up with emerging trends in front-end development and modern web technologies. | Mentored junior engineers and kept up with modern web technologies and frameworks.                            |\n| Experiment with new tools, frameworks, and methodologies to improve development efficiency. | Experience with various frameworks (React, Vue, etc.) and CI/CD tools (Docker, Jenkins).                     |\n| Document codebase clearly for future maintenance and teamwork.                  | Established comprehensive UI/UX handbook and design guidelines for onboarding teams.                          |\n| Utilize version control systems (e.g., Git) for effective code management.     | Proficient in Git, GitHub, and GitLab; used for collaboration and version control in multiple projects.      |\n| Bachelor’s degree in Computer Science, Web Development, or a related field.    | B.Sc. in Computer Science from The University of Tehran.                                                     |\n| Proven experience in front-end development (portfolio or GitHub profile preferred). | Senior Frontend Engineer at Apple and Shopee; GitHub profile available for review.                           |\n| Proficiency in HTML5, CSS3, and JavaScript (ES6+).                             | Proficient in HTML5, CSS3, and JavaScript; experience with ES6+ features.                                   |\n| Experience with frameworks/libraries such as React, Angular, or Vue.js.        | Experience with React, Vue, and other frameworks (Svelte, NextJS, etc.).                                     |\n| Familiarity with CSS pre-processors like SASS or LESS.                         | Experienced with Sass and Less for styling.                                                                   |\n| Knowledge of version control systems like Git.                                  | Proficient in Git, GitHub, and GitLab for version control.                                                   |\n| Strong problem-solving and analytical skills.                                   | Demonstrated problem-solving skills through stakeholder collaboration and project execution.                  |\n| Ability to collaborate effectively with cross-functional teams.                 | Collaborated with cross-functional teams at Apple and Shopee.                                                |\n| Attention to detail and focus on user experience.                               | Established design guidelines and UI Kit to enhance user experience.                                         |\n| Experience in Containerization and CI/CD pipelines.                             | Experience with Docker and CI/CD tools like Jenkins and Travis.                                              |\n| Experience in Agile development practices.                                      | Worked in Agile methodologies at Apple and Shopee.                                                            |\n| 3+ years of front-end development experience.                                   | Over 5 years of experience in front-end development across multiple companies.                                |\n| Experience in Agile or Scrum development environments.                          | Experience in Agile methodologies at Apple and Shopee.                                                        |\n| Ability to commute/relocate: Karachi.                                          | Currently located in Montreal, QC, Canada; willing to relocate.                                              |\n```"""
# Generate the merged JSON
# merged_json = merge_questions_and_answers(correct_answers, false_answers)
# print(merged_json)

# merged_json = merge_questions_and_answers(correct_answers, false_answers)
# print(getCleanMarkDownTable(markdown))