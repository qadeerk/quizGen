from langchain.prompts import PromptTemplate
        
quiz_generation_template = PromptTemplate(template="""
    Generate a question and a answer out of the below test, the answer should be concise as possible 
    -----
    question: {question}
    Answer: {Answer}
    -----
    Format output in json 
    {
        option1:[value], 
        option2:[value],
        option3:[value],
    }
"""
,input_variable=['question','Answer'])
