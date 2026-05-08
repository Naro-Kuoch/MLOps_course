
from src.register import enter_data

def test_input(monkeypatch):

    inputs = iter([
        "Alice",
        "alice@company.com",
        "alice12345"
    ])
    # replace input()
    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )
    assert enter_data() != None

