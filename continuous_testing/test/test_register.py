# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
from src.register import enter_data
import pytest
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

    try:
        enter_data()
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")

