from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import RunnableParallel

def parallelExecution(list,processor):
    runnables = {
    str(index): RunnableLambda(lambda input, index=index, item=item: processor(index, item))
    for index, item in enumerate(list)
    }
    parallel_inputs = {str(index): None for index, _ in enumerate(list)}
    parallel_executor = RunnableParallel(runnables)
    return parallel_executor.invoke(parallel_inputs)