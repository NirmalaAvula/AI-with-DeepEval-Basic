from deepeval.test_case import LLMTestCase, SingleTurnParams
from deepeval.metrics import GEval
from deepeval.models import OllamaModel


# Ollama model used as the GEval judge
judge_model = OllamaModel(
    model="llama3.1:latest"
)


# GEval metric
hallucination_metric = GEval(
    name="Hallucination Detection",

    criteria="""
    Evaluate whether the actual output is factually correct
    based on the expected output.

    Give a high score when the answer is correct and does not
    introduce unsupported facts.

    Give a low score when the answer contains factual errors,
    contradictions, or unsupported information.
    """,

    evaluation_params=[
        SingleTurnParams.INPUT,
        SingleTurnParams.ACTUAL_OUTPUT,
        SingleTurnParams.EXPECTED_OUTPUT
    ],

    model=judge_model,

    threshold=0.7
)


def evaluate_response(question, ground_truth, llm_response):

    # Create DeepEval test case
    test_case = LLMTestCase(
        input=question,
        actual_output=llm_response,
        expected_output=ground_truth
    )

    print("Evaluating...")

    # Run GEval
    hallucination_metric.measure(test_case)

    # Get GEval results
    score = hallucination_metric.score
    reason = hallucination_metric.reason

    # PASS / FAIL
    if score >= 0.7:
        result = "PASS"
    else:
        result = "FAIL"

    print("\nGEval Evaluation:")
    print("Score:", score)
    print("Result:", result)
    print("Reason:", reason)

    return score, result, reason