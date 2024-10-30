import pytest
from working import validate

def test_validate():
    assert validate("9 AM to 5 PM") == "09:00 to 17:00"
    assert validate("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert validate("10 PM to 8 AM") == "22:00 to 08:00"
    assert validate("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_value_error():
    with pytest.raises(ValueError):
        validate("9AM - 5PM")
    with pytest.raises(ValueError):
        validate("09:00 to 17:00")
    with pytest.raises(ValueError):
        validate("15:00 AM to 25:00 PM")
    with pytest.raises(ValueError):
        validate("9:60 AM to 5:60 PM")
