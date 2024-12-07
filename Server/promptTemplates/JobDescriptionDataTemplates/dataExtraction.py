from langchain.prompts import PromptTemplate
        
quiz_generation_template = PromptTemplate(template="""
    You are an interviewer who has to generate a list titles of different interview sections that the candidate will go through these sections will be evaluate different skills that are part of the job description.
    keep the list consise and to the point
    -----
    job Description: 
    {jobDescription}
    -----
    Format output in json 
    {
        section1:[title], 
        section2:[title],
        section3:[title],
        ...
    }
"""
,input_variable=['jobDescription'])