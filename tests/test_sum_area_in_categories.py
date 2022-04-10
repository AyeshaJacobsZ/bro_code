import pandas as pd
from src.category import Category


class TestSumAreaInCategories:
    def test_sum_area_in_categories_when_called_returns_correct_sum_of_area(self):
        data = pd.DataFrame([[2.280, 3, 2], [1.510, 3, 1]], columns=['Calculated Area m\u00b2', 'category', 'Count'])
        duct = Category(data)
        sum_category = duct.sum_area_in_categories(duct.data)
        assert sum_category['Calculated Area m\u00b2'].iloc[0] == 3.79

    def test_sum_area_in_categories_is_not_string(self):
        data = pd.DataFrame([[2.280, 3, 2], [1.510, 3, 1]], columns=['Calculated Area m\u00b2', 'category', 'Count'])
        duct = Category(data)
        sum_category = duct.sum_area_in_categories(duct.data)
        sum_category_type = type(sum_category['Calculated Area m\u00b2'].iloc[0])
        assert sum_category_type != str
