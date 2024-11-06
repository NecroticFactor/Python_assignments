import pytest
from seasons import Human
from unittest.mock import patch
from datetime import date

def test_date_validation():
    # Test invalid date formats
    with pytest.raises(SystemExit):
        Human("07-07-1999")  # Invalid date format
    with pytest.raises(SystemExit):
        Human("January 1, 1999")  # Another invalid date format

    # Test valid date format
    person = Human("1999-07-07")
    assert person.date_of_birth == date(1999, 7, 7)

def test_calculate_minutes():
    person = Human("1999-07-07")

    # Mock today's date to ensure consistency
    with patch('seasons.date') as mock_date:
        mock_date.today.return_value = date(2023, 10, 4)  # Mocked current date
        assert person.calculate_minutes() == (24 * 60 * (date(2023, 10, 4) - date(1999, 7, 7)).days)

def test_wordify():
    person = Human("1999-07-07")
    assert person.wordify(13278240) == "Thirteen million, two hundred seventy-eight thousand, two hundred forty minutes"
