from langchain.prompts import PromptTemplate
        
question_generation_template = PromptTemplate(template="""
    Generate a question and a answer out of the below test, the answer should be concise as possible 
    -----
    facts: {text}
    -----
    Format output in object 
        "Question":, 
        "Answer":
"""
,input_variable=['text'])
