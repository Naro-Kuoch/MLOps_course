
from src.register import enter_data


def test_input(monkeypatch):
    # Simulate user input for a registration flow.
    inputs = iter([
        "Alice",
        "alice@company.com",
        "alice12345!" # Valid password with all required characters.
        "25"
    ])

    # Patch builtins.input so enter_data() consumes our predefined values.
    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    # The function should return a non-None registration dictionary.
    assert enter_data() is not None

