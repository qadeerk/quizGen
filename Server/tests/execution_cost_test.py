from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.callbacks import get_openai_callback


# Load the .env file
load_dotenv()

# Initialize OpenAI model
llm = ChatOpenAI(model_name="gpt-4", temperature=0)

# Example prompt
prompt = "Explain quantum physics in simple terms."

# Track token usage and cost
with get_openai_callback() as callback:
    response = llm.invoke(prompt)
    print(response)

    # Token usage and cost
    print(f"Total Tokens: {callback.total_tokens}")
    print(f"Prompt Tokens: {callback.prompt_tokens}")
    print(f"Completion Tokens: {callback.completion_tokens}")
    print(f"Total Cost (USD): ${callback.total_cost}")