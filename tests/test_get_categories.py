import pytest
import pandas as pd
from src.category import Category

class TestGetCategories:
    def test_get_categories(self):
        data = pd.DataFrame([700, 1000], columns=['min_width', 'min_height'])
        duct = Category(data)
        category = duct.get_categories(data)
        assert category == 3
