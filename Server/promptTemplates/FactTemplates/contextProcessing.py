from langchain.prompts import PromptTemplate

#  if the document is very big it would be a good idea to break the document into smaller parts and then extract facts from each part. This will help in coverage of the segments.
context_classification_template = PromptTemplate(template="""
    classify the below text into three different types paragraphs with no headings, heading with short description, heading with long description
    -----
    text: {text}
    -----
    output should be only three
    [
        [section Title]:[text], 
        [section Title]:[text],
        [section Title]:[text],
        ...
    ]
"""
,input_variable=['text'])

