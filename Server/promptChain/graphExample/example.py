from langgraph.graph import Graph
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load the .env file
load_dotenv()

model = ChatOpenAI(model_name="gpt-4o-mini",
                 temperature= 0.0)

def function1(input):
    task = "you task is to tell a fact about : " + input
    return model.invoke(task).content

def function2(input):
    return "agent says: " + input

workflow = Graph()

workflow.add_node("node1", function1)
workflow.add_node("node2", function2)

workflow.add_edge("node1", "node2")

workflow.set_entry_point("node1")
workflow.set_finish_point("node2")

app = workflow.compile()
print(app.invoke("karachi"))