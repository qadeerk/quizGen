from langchain.prompts import PromptTemplate

context_extraction_template = PromptTemplate(template="""
Given a list of skills, generate a detailed and unique context for each skill. The context should provide comprehensive information about the skill to be used for quiz generation. Follow these guidelines:

1. **Structure**: for the given skillset, create paragraph of concepts that an expert in that skill should know. The context should include:
   - few expert level concept of a skill or tool that is consicely defided.
   - Key principles related to that skill or tool that an expert should know.

2. **Depth**: Ensure the context is rich in detail and avoids generic statements. Include any nuances or specifics that would make the context unique and informative.

3. **Output Format**: The output should be structured as follows:

[Skill Name]: [Detailed Context]
[Skill Name]: [Detailed Context] ...      

Generate context only for the provided skills.

4. **Constraints**:
   - Avoid using contexts from external references.
   - Avoid code snippets.
   - Avoid asking simple questions like what a specific tool does.
   - Ensure the descriptions are written in an educational and engaging tone suitable for fact generation.

Input:
skillset: {skillset}
                                             
Expected Output:

- [Skill Name]: [Detailed Context]
- [Skill Name]: [Detailed Context]
...                           
""",
input_variables=["skillset"])

