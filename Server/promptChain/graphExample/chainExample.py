from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.graph import Graph
from dotenv import load_dotenv


# Load the .env file
load_dotenv()

# Initialize the LLM
llm = ChatOpenAI(model_name="gpt-4")

# Fact Extraction Prompt
fact_extraction_prompt = PromptTemplate(
    input_variables=["paragraph"],
    template="Extract a list of key facts from the following paragraph:\n\n{paragraph}\n\nOutput each fact as an item in an array."
)

# Fact-to-Question Prompt
fact_to_question_prompt = PromptTemplate(
    input_variables=["fact"],
    template="Convert the following fact into a meaningful question:\n\nFact: {fact}\n\nQuestion:"
)

# Define the graph
lang_graph = Graph()

# Add the fact extraction node
lang_graph.add_node(
    node_id="extract_facts",
    func=lambda inputs: llm.generate(
        fact_extraction_prompt.format(paragraph=inputs["paragraph"])
    ),
    input_keys=["paragraph"],
    output_key="facts",
)

# Add the question generation node
lang_graph.add_node(
    node_id="generate_questions",
    func=lambda inputs: [
        llm.generate(fact_to_question_prompt.format(fact=fact))
        for fact in eval(inputs["facts"])  # Convert stringified list to Python list
    ],
    input_keys=["facts"],
    output_key="questions",
)

# Link the nodes
lang_graph.link_nodes("extract_facts", "generate_questions")

# Input paragraph
paragraph = """
Artificial intelligence (AI) is a branch of computer science that aims to create machines that can perform tasks 
that typically require human intelligence. Examples include visual perception, speech recognition, decision-making, 
and language translation.
"""

# Run the graph
inputs = {"paragraph": paragraph}
outputs = lang_graph.run(inputs)

# Output the Questions
for idx, question in enumerate(outputs["questions"], 1):
    print(f"Question {idx}: {question}")