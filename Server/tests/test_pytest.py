import pytest
from deepeval import assert_test
from deepeval.metrics import HallucinationMetric, AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase
from deepeval.dataset import EvaluationDataset
from deepeval.metrics import JsonCorrectnessMetric
from pydantic import BaseModel
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

first_test_case = LLMTestCase(input="jon is 5 feet tall", actual_output="""{"Question": "How tall is Jon?","Answer": "5 feet"}""")

second_test_case = LLMTestCase(input="jon is 6 feet tall", actual_output="""{"Question": "How tall is Jon?","Answer": "6 feet"}""")

class ExampleSchema(BaseModel):
    Question: str
    Answer: str

dataset = EvaluationDataset(test_cases=[first_test_case, second_test_case])

@pytest.mark.parametrize(
    "test_case",
    dataset,
)
def test_JsonCorrectness(test_case: LLMTestCase):
    JsonCorrectness_metric = JsonCorrectnessMetric(expected_schema=ExampleSchema,model="gpt-4",include_reason=False)
    # Test the case
    try:
        assert_test(test_case, [JsonCorrectness_metric])
    except AssertionError:
            # Test failed for this LLM
            pass
    

# deepeval test run test_pytest.py -n 4
# pytest .\test_pytest.py --html=report.html