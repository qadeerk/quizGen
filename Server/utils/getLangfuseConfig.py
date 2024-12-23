from langfuse.callback import CallbackHandler

langfuse_handler = CallbackHandler(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST")
)

def getLangChainConfig():
    return {"callbacks": [langfuse_handler]}

def getLangfuseHandeler():
    return langfuse_handler