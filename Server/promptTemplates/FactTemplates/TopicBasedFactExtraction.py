from langchain.prompts import PromptTemplate

#  if the document is very big it would be a good idea to break the document into smaller parts and then extract facts from each part. This will help in coverage of the segments.
quiz_generation_template = PromptTemplate(template="""
    break the following text into smaller none overlaping sections and generate a list of sections, assign a title to each section that best describes the content of the section
    -----
    text: {text}
    -----
    Format output in object that can be parsed in json
    [
        [section Title]:[text], 
        [section Title]:[text],
        [section Title]:[text],
        ...
    ]
"""
,input_variable=['text'])
