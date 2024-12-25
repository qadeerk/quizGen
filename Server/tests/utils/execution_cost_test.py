from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.callbacks import get_openai_callback
from time import perf_counter

# Load the .env file
load_dotenv()

# Initialize OpenAI model
llm = ChatOpenAI(model_name="gpt-4", temperature=0)

# Example prompt
prompt = "Explain quantum physics in simple terms."

# Track token usage and cost
def get_execution_cost(llm, prompt):
    with get_openai_callback() as callback:
        # print("----starting llm invocation----")
        start_time = perf_counter()  # Record the start time
        response = llm.invoke(prompt)
        end_time = perf_counter()  # Record the end time
        latency = end_time - start_time  # Calculate latency in seconds
        # print("----llm invocation  complete---")
        return {
            "response": response,
            "output": response.content,
            "total_tokens": callback.total_tokens,
            "prompt_tokens": callback.prompt_tokens,
            "completion_tokens": callback.completion_tokens,
            "latency_seconds": latency,
            "total_cost": f"${callback.total_cost:.15f}".rstrip('0').rstrip('.')
        }

# Example usage
# result = get_execution_cost(llm, prompt)
# print(f"Output: {result}")
# print(f"Total Tokens: {result['total_tokens']}")
# print(f"Prompt Tokens: {result['prompt_tokens']}")
# print(f"Completion Tokens: {result['completion_tokens']}")
# print(f"latency: {result['latency_seconds']}")
# print(f"Total Cost (USD): ${result['total_cost']}")