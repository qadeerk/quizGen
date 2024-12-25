from langchain.prompts import PromptTemplate

skill_Extraction_template = PromptTemplate(template="""
    Extract a list of skill set based on the below description 
    skills should include tools, frameworks , technologies , interpersonal/transferable, managerial 
    -----
    job Description: 
    {jobDescription}
    -----
    These skill should not include work type, certifications and background checks 
    Format output in json 
    [
        {{
            "category": name,
            "skills": []
        }}
    ]
"""
,input_variable=['jobDescription'])

#  TODO : can be used to compare distance from CV with better acuracy. (Remove from final code if not used)
Responsiblities_Extraction_template = PromptTemplate(template="""
    Extract a list of responsibility set based on the below job description 
    Merge skills and responsibilities and generate a new list of responsibilities  
    -----
    job Description: 
    {jobDescription}
    -----
    Output should be in json array
    []
"""
,input_variable=['jobDescription'])

#  TODO : (Remove from final code if not used)
Qulification_Extraction_template = PromptTemplate(template="""
    Extract a list of Qualification set based on the below job description 
    Qualification should not include tools, frameworks , technologies and responsibilities and objectives 
    -----
    job Description: 
    {jobDescription}
    -----
    These skill should only include degree , certifications , years of experience and any clearances 
    Output should be in json object
    {
    Education :
    Experience : 
    Certifications : []
    }
"""
,input_variable=['jobDescription'])