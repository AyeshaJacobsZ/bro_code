import pytest
import pandas as pd
from src.duct import Duct


class TestGetCalculatedArea:

    def test_get_calculated_area(self):
        duct = Duct()
        calculated_area = duct.get_calculated_area(2, 5, 0)
        assert calculated_area == 10


