import pytest
import pandas as pd
from src.category import Category


def test_sum_area_in_categories():
    data = pd.DataFrame([[2.280, 3, 2], [1.510, 3, 1]], columns=['Calculated Area m\u00b2', 'category', 'Count'])
    duct = Category(data)
    sum_category = duct.sum_area_in_categories(duct.data)
    assert sum_category['Calculated Area m\u00b2'].iloc[0] == 3.79
