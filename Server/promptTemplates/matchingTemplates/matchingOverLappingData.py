from langchain.prompts import PromptTemplate
        
overlaping_data_template = PromptTemplate(template="""
    You are given a job description and CV data in markdown generate a table witch matching requirements in the job description that are in the CV
    ------------
    Job Description :
    {jobDescription}
    --------------
    CV :
    {cvData}
    --------------
    output table markdown format only
"""
,input_variable=['jobDescription','cvData'])

non_overlaping_job_description_template = PromptTemplate(template="""
    You are given a job description and CV data in markdown generate a table which are not matching the requirements in job description
    ------------
    Job Description :
    {jobDescription}
    ------------
    CV :
    {cvData}
    ------------
    output table markdown format only
"""
,input_variable=['jobDescription','cvData'])
