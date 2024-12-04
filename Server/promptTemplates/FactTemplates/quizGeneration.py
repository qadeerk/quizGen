from langchain.prompts import PromptTemplate
        
quiz_generation_template = PromptTemplate(template="""
    Use the following Question and Answer to generate three false options for a quiz as output these options should not be the correct answer to the question
    -----
    Question: {Question}
    Answer: {Answer}
    -----
    Format output in object that can be parsed in json
    [
        1:[value1],
        2:[value2],
        3:[value3],
    ]
"""
,input_variable=['Question','Answer'])
