from olib.solutions import ask_model


def test_ask_model():
    assert "Paris" in ask_model("What is the capital of France?")
