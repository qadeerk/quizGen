from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from dotenv import load_dotenv
import os
load_dotenv()

# arm=AnswerRelevancyMetric(threshold=0.7)

# test_case=LLMTestCase(
#     input="What if these shoes doesn't fit me?",
#     actual_output="We offer a 30-day full refund at no extra costs",
#     retrieval_context=["All customers are eligible for a 30-day full refund at no costs."]
# )

# evaluate([test_case],[arm])


from deepeval.metrics import ToxicityMetric
from deepeval.test_case import LLMTestCase

metric = AnswerRelevancyMetric(
    threshold=0.7,
    model="gpt-4o",
    include_reason=True
)
test_case = LLMTestCase(
    input="""
A Class is a user-defined blueprint or prototype from which objects are created. It represents the set of properties or methods that are common to all objects of one type. Using classes, you can create multiple objects with the same behavior instead of writing their code multiple times. This includes classes for objects occurring more than once in your code. In general, class declarations can include these components in order: 
Modifiers: A class can be public or have default access (Refer to this for details).
Class name: The class name should begin with the initial letter capitalized by convention.
Body: The class body is surrounded by braces, { }.
What is Object?
An Object is a basic unit of Object-Oriented Programming that represents real-life entities. A typical Java program creates many objects, which as you know, interact by invoking methods. The objects are what perform your code, they are the part of your code visible to the viewer/user. An object mainly consists of: 
State: It is represented by the attributes of an object. It also reflects the properties of an object.
Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
Identity: It is a unique name given to an object that enables it to interact with other objects.
Method: A method is a collection of statements that perform some specific task and return the result to the caller. A method can perform some specific task without returning anything. Methods allow us to reuse the code without retyping it, which is why they are considered time savers. In Java, every method must be part of some class, which is different from languages like C, C++, and Python. """,
    # Replace this with the actual output from your LLM application
    actual_output="A Class is a user-defined blueprint or prototype from which objects are created, representing common properties or methods.', 'An Object is a basic unit of Object-Oriented Programming that represents real-life entities and interacts by invoking methods.', 'An Object consists of State (attributes), Behavior (methods), and Identity (unique name).', 'A Method is a collection of statements that perform specific tasks and can return results, allowing code reuse.', 'In Java, every method must be part of a class, unlike in languages like C, C++, and Python."
)

metric.measure(test_case)
print(metric.score)
print(metric.reason)

evaluate([test_case], [metric])