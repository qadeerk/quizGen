from langchain.prompts import PromptTemplate
        
quiz_generation_template = PromptTemplate(template="""
    break the following
    -----
    text: {text}
    -----
    Format output in json 
    {
        [Topic Name]:[text], 
        [Topic Name]:[text],
        [Topic Name]:[text],
        ...
    }
"""
,input_variable=['text'])
