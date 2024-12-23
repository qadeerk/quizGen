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
def get_execution_cost(llm, prompt):
    with get_openai_callback() as callback:
        response = llm.invoke(prompt)
        # print(response)
        return {
            "output": response.content,
            "total_tokens": callback.total_tokens,
            "prompt_tokens": callback.prompt_tokens,
            "completion_tokens": callback.completion_tokens,
            "total_cost": f"${callback.total_cost:.15f}".rstrip('0').rstrip('.')
        }

# Example usage
# result = get_execution_cost(llm, prompt)
# print(f"Output: {result['output']}")
# print(f"Total Tokens: {result['total_tokens']}")
# print(f"Prompt Tokens: {result['prompt_tokens']}")
# print(f"Completion Tokens: {result['completion_tokens']}")
# print(f"Total Cost (USD): ${result['total_cost']}")