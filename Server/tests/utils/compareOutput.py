import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Add the 'tests' directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from deepeval.metrics import BaseMetric
from deepeval.test_case import LLMTestCase
from sentenceSimilarityUtils import calculate_similarity  # Absolute import

def generate_hypothetical_score(test_case: LLMTestCase) -> float:
    # This is a hypothetical function that generates a score
    # based on the test case input and output
    print(test_case.input)
    print(test_case.actual_output)
    print(test_case.expected_output)
    return calculate_similarity(test_case.actual_output, test_case.expected_output)

def generate_hypothetical_reason(test_case: LLMTestCase) -> str:
    # This is a hypothetical function that generates a reason
    # based on the test case input and output
    return "reasoning not implemented"

async def async_generate_hypothetical_score(test_case: LLMTestCase) -> float:
    # This is a hypothetical function that generates a score
    # based on the test case input and output
    print(test_case.input)
    print(test_case.actual_output)
    print(test_case.expected_output)
    return calculate_similarity(test_case.actual_output, test_case.expected_output)

async def async_generate_hypothetical_reason(test_case: LLMTestCase) -> str:    
    # This is a hypothetical function that generates a reason
    # based on the test case input and output
    return "reasoning not implemented"

class JsonSimilarityScoreMetric(BaseMetric):
    def __init__(
        self,
        threshold: float = 0.5,
        evaluation_model: str = "gpt4",
        include_reason: bool = True,
        strict_mode: bool = True,
        async_mode: bool = True
    ):
        self.threshold = threshold
        # Optional
        self.evaluation_model = evaluation_model
        self.include_reason = include_reason
        self.strict_mode = strict_mode
        self.async_mode = async_mode
    
    @property
    def __name__(self):
        return "My Custom Metric"
    
    def measure(self, test_case: LLMTestCase) -> float:
        # Although not required, we recommend catching errors
        # in a try block
        try:
            self.score = generate_hypothetical_score(test_case)
            if self.include_reason:
                self.reason = generate_hypothetical_reason(test_case)
            self.success = self.score >= self.threshold
            return self.score
        except Exception as e:
            # set metric error and re-raise it
            self.error = str(e)
            raise

    async def a_measure(self, test_case: LLMTestCase) -> float:
        # Although not required, we recommend catching errors
        # in a try block
        try:
            self.score = await async_generate_hypothetical_score(test_case)
            if self.include_reason:
                self.reason = await async_generate_hypothetical_reason(test_case)
            self.success = self.score >= self.threshold
            return self.score
        except Exception as e:
            # set metric error and re-raise it
            self.error = str(e)
            raise
        
    def is_successful(self) -> bool:
        if self.error is not None:
            self.success = False
        else:
            return self.success