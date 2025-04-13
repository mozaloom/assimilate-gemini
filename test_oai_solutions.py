from olib.solutions import ask_model, create_code


def test_ask_model():
    assert "Paris" in ask_model("What is the capital of France?")

def test_create_code():
    assert "def" in create_code("Python", "Write a function that adds two numbers.")
