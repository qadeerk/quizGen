# write code to which will return a list of llms to evaluate
#  initially it can be gpt3.5 turbo and gpt4o-mini
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

gpt4 = ChatOpenAI(model_name="gpt-4", temperature=0)
gpt4_mini = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
gpt3_turbo = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
ChatAnthropicllm = ChatAnthropic(model_name="gpt-4", temperature=0)

def getOpenAIModelList():
    return [gpt3_turbo, gpt4_mini]

def getModelList():
    return [gpt3_turbo, gpt4_mini, gpt4, ChatAnthropicllm]