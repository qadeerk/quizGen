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


extract_cv_topics_template = """
Extract the key topics and skills from the following CV data and present them as a list:
{cv_data}
"""

extract_job_description_topics_template = """
Extract the key topics and requirements from the following job description and present them as a list:
{job_description}
"""

generate_interview_sections_template = """
Based on the following job description, generate different sections of an interview and present them as a list of section titles and descriptions:
{job_description}
"""

breakdown_data_into_topics_template = """
Break down the following data into different topics with text related to each topic, and present it in JSON format:
{data}
"""

prompt_template = PromptTemplate(template=template,input_variable=['text'])
prompt_template = PromptTemplate(template=template,input_variable=['text'])