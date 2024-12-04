from langchain.prompts import PromptTemplate
        
      
fact_extraction_template = PromptTemplate(template="""
    you are a sumiriser and you need extract main facts from the text below
    -----
    Text:{text}
    -----
    Format output as an array
    [
        "fact1",
        "fact2",
        "fact3"
    ]
"""
,input_variable=['text'])
