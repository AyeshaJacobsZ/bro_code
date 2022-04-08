from src.duct import Duct
import pandas as pd


def test_get_minimum_width():
    data = pd.DataFrame([[800, 200, 450, 200, 450, 200]],
                        columns=['width_1', 'height_1', 'width_2', 'height_2', 'width_3', 'height_3'])
    duct = Duct()
    minimum_value = duct.get_minimum_width_and_height(data)['min_width'].iloc[0]

    assert minimum_value == 450


def test_get_minimum_height():
    data = pd.DataFrame([[800, 200, 450, 200, 450, 200]],
                        columns=['width_1', 'height_1', 'width_2', 'height_2', 'width_3', 'height_3'])
    duct = Duct()
    minimum_value = duct.get_minimum_width_and_height(data)['min_height'].iloc[0]

    assert minimum_value == 200
