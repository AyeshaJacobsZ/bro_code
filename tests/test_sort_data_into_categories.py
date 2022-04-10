import pytest
import pandas as pd
from src.category import Category


class TestGetCategories:
    def test_sort_data_into_categories_when_called_returns_correct_category_number(self):
        data = pd.DataFrame([[700, 1000]], columns=['min_width', 'min_height'])
        duct = Category(data)
        category = duct.sort_data_into_categories(data)
        assert category['category'].iloc[0] == 3

    def test_sort_data_into_categories_returns_less_than_five(self):
        data = pd.DataFrame([[700, 1000]], columns=['min_width', 'min_height'])
        duct = Category(data)
        category = duct.sort_data_into_categories(data)
        assert category['category'].iloc[0] <= 5
