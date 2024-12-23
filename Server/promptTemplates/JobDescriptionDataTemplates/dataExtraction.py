from langchain.prompts import PromptTemplate

# section extraction
# Job Title
# Job Summary
# Key Responsibilities/Duties
# Qualifications
# Skills and Competencies
# Experience Requirements
# Working Conditions

  
quiz_generation_template = PromptTemplate(template="""
    From the job description below extract the list of responsiblities, qualification, Skills , and job location, follow the below instructions
    - for skills identify interpersonal skills also like teamwork, leadership 
    -----
    job Description: 
    {jobDescription}
    -----
    Format output in json 
    {
        responsiblities: {}, 
        qualification:{},
        Skills:{},
        job location:{}
    }
"""
,input_variable=['jobDescription'])