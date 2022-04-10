from src.duct import Duct
import pandas as pd


class TestGetMinimumWidthAndHeight:
    def test_get_minimum_width_when_called_returns_correct_minimum_width(self):
        data = pd.DataFrame([[800, 200, 450, 200, 450, 200]],
                            columns=['width_1', 'height_1', 'width_2', 'height_2', 'width_3', 'height_3'])
        duct = Duct()
        minimum_value = duct.get_minimum_width_and_height(data)['min_width'].iloc[0]

        assert minimum_value == 450

    def test_get_minimum_height_when_called_returns_correct_minimum_height(self):
        data = pd.DataFrame([[800, 200, 450, 200, 450, 200]],
                            columns=['width_1', 'height_1', 'width_2', 'height_2', 'width_3', 'height_3'])
        duct = Duct()
        minimum_value = duct.get_minimum_width_and_height(data)['min_height'].iloc[0]

        assert minimum_value == 200

    def test_minimum_width_is_not_string(self):
        data = pd.DataFrame([[800, 200, 450, 200, 450, 200]],
                            columns=['width_1', 'height_1', 'width_2', 'height_2', 'width_3', 'height_3'])
        duct = Duct()
        minimum_width = duct.get_minimum_width_and_height(data)['min_width'].iloc[0]
        minimum_width_type = type(minimum_width)
        assert minimum_width_type != str

    def test_minimum_height_is_not_string(self):
        data = pd.DataFrame([[800, 200, 450, 200, 450, 200]],
                            columns=['width_1', 'height_1', 'width_2', 'height_2', 'width_3', 'height_3'])
        duct = Duct()
        minimum_height = duct.get_minimum_width_and_height(data)['min_height'].iloc[0]
        minimum_height_type = type(minimum_height)
        assert minimum_height_type != str
