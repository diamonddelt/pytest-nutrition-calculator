import pytest
from calculator import Calculator

@pytest.fixture
def create_calculator():
    return Calculator()

def test_meals_are_logged():
    c = create_calculator()
    c.log_meal("Test Meal", 3, 3, 3)
    assert c.meals_eaten_today == ['Test Meal']

def test_null_value_raises_exception_on_log_meal():
    c = create_calculator()
    with pytest.raises(Exception):
        c.log_meal(None, None, None, None)

