import pytest
import pandas as pd
from src.duct import Duct


class TestGetCalculatedArea:

    def test_get_calculated_area_when_called_returns_correct_area(self):
        duct = Duct()
        calculated_area = duct.get_calculated_area(2, 5, 0)
        assert calculated_area == 10

    def test_calculated_area_returns_not_string(self):
        duct = Duct()
        calculated_area = duct.get_calculated_area(2, 5, 0)
        calculated_area_type = type(calculated_area)
        assert calculated_area_type != str