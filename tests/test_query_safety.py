from app.validation.guardrails import enforce_guardrails
import pytest

def test_forbidden_sql_raises_error():
    with pytest.raises(ValueError, match="Forbidden SQL operation"):
        enforce_guardrails("DROP TABLE users")
