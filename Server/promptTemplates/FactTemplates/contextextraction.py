from langchain.prompts import PromptTemplate

context_extraction_template = PromptTemplate(template="""
Given a list of skills, generate a detailed and unique context for each skill. The context should provide comprehensive information about the skill to be used for quiz generation. Follow these guidelines:

1. **Structure**: For each skill, create a separate paragraph that describes:
   - A clear definition of the skill.
   - Key principles or concepts associated with the skill.
   - Common applications or use cases in real-world scenarios.
   - Any relevant technologies, tools, or methods often associated with the skill.

2. **Depth**: Ensure the context is rich in detail and avoids generic statements. Include any nuances or specifics that would make the context unique and informative.

3. **Output Format**: The output should be structured as follows:

[Skill Name]: [Detailed Context]
[Skill Name]: [Detailed Context] ...      

Generate context only for the provided skills.

4. **Constraints**:
   - Avoid using examples or contexts from external references.
   - Ensure the descriptions are written in an educational and engaging tone suitable for fact generation.

Input:
skillset: {skillset}
                                             
Expected Output:

- [Skill Name]: [Detailed Context]
- [Skill Name]: [Detailed Context]
...                           
""",
input_variables=["skillset"])

