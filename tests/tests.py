from src.calculations import calc
from tests.data import expected_output, get_input_data


def test_calc():
    assert calc(*get_input_data()) == expected_output
