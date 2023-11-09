from pprint import pprint

from src.calculations import calc
from tests.data import get_input_data

if __name__ == '__main__':
    pprint(calc(*get_input_data()))
