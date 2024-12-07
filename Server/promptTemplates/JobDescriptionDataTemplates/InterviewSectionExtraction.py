from langchain.prompts import PromptTemplate

leftJoin_data_template = PromptTemplate(template="""
    You are a professional interviewer tasked to design interview sections based on the responsibilities skillset, duties , role and job requirements.
    this is going to be a screening interview list only the section name use the examples to generate similar sections.
    -----------
    Example Interview sections
    HTML/javascript/css
    figma
    c#,java,c++,python
    Collaboration and Communication Skills
    Version Control and Code Management
    micro front-end
    microservices
    Load testing/performance 
    ------------
    Job Description :
    {jobDescription}
    ------------
    output in list format section names
"""
,input_variable=['jobDescription'])