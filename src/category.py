import pandas as pd
import numpy as np

"""
Category class:
- gets cleaned data 1
- places ducts into categories using size columns 1
- calculates total m^2 for that category in that duct file 1
- calculates total amount in R for BOQ (either dictionary or dataframe format) 1
- information gets passed to BOQ 0
"""


class Category:
    def __init__(self, data):
        self.data = data

    def get_categories(self, width, height):

        maximum = max(width, height)
        addition = width + height
        if maximum < 750 and addition <= 1150:
            category = 1
        elif maximum < 750 and addition > 1150:
            category = 2
        elif 750 <= maximum < 1350:
            category = 3
        elif 1350 <= maximum < 2100:
            category = 4
        elif 2100 <= maximum:
            category = 5

        return category

    def sort_data_into_categories(self, data):
        data['category'] = data.apply(lambda x: self.get_categories(x['min_width'], x['min_height']), axis=1)
        return data

    def sum_area_in_categories(self, data):
        summed_categories = data[['Area', 'category', 'Count']].groupby(['category']).sum()
        return summed_categories

    def categorize(self):
        for key, value in self.data.items():
            categories = self.sort_data_into_categories(value)
            categories = self.sum_area_in_categories(categories)
            self.data[key] = categories

        return self.data

    def boq(self):
        data = self.categorize()
        rate = {1: 1, 2: 2.5, 3: 4, 4: 5, 5: 6}
        result = {}

        for key, value in data.items():
            # print(key)
            # print(value)
            value = value.reset_index()
            value['rate'] = value['category'].map(rate)
            value['cost'] = value['Area'] * value['rate']
            value.drop(columns=["Area"], inplace=True)
            value.columns = ['category', 'quantity', 'rate', 'cost']
            total = value['cost'].sum(axis=0)
            last_row = pd.DataFrame([['total', total, '', '']], columns=['category', 'quantity', 'rate', 'cost'])
            value = pd.concat([value, last_row], axis=0)
            result[key] = value

        return result




