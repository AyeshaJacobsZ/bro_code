import pandas as pd
import pytest
from duct import Duct

class TestClass(pytest.TestCase):

    def test_convert_to_float(self):
        data = pd.DataFrame([2, '2.280 m\u00b2', '0.000 m\u00b2'], columns=['Count', 'Area', 'Surface Area'])
        duct_1 = Duct(data)
        float_data = duct_1.convert_to_float()
        data_types = float_data.dtypes()
        float_series = pd.Series([float, float, float])
        self.assertTrue()

    def test_clear_nan_rows(self):
        pass

    def test_get_calculated_area(self):
        data = pd.DataFrame([2,5,0], columns = ['Count', 'Area', 'Surface Area'])
        duct = Duct(data)
        calculated_area = duct.get_calculated_area()
        self.assertEqual(calculated_area, 10)

    def test_calculate_total_area(self):
        pass

    def test_sort_categories(self):
        data = pd.DataFrame([700,1000], columns = ['min_width', 'min_height'])
        duct = Category(data)
        category = duct.sort_categories()
        self.assertEqual(category, 3)

    def test_sum_area_in_categories(self):
        data = pd.DataFrame([[2.280,3],[1.510,3]], columns = ['Area', 'category'])
        duct = Category(data)
        sum_category = duct.sum_area_in_categories()
        self.assertEqual(sum_category, 3.790)
