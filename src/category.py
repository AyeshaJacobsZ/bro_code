import pandas as pd


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
        print(data)
        return data

    def sum_area_in_categories(self, data):
        summed_categories = data[['Calculated Area m\u00b2', 'category', 'Count']].groupby(['category']).sum()
        return summed_categories

    def categorize(self):
        for key, value in self.data.items():
            categories = self.sort_data_into_categories(value)
            if key == 'Duct Fitting Schedule Low Pressure Insulated Cladded Rect.csv':
                value.to_csv('check.csv')
            categories = self.sum_area_in_categories(categories)
            self.data[key] = categories

        return self.data

    def calculate_rate(self):
        data = self.categorize()
        rate = {1: 1, 2: 2.5, 3: 4, 4: 5, 5: 6}
        result = {}

        for key, value in data.items():
            value = value.reset_index()
            value['rate'] = value['category'].map(rate)
            value['cost'] = value['Calculated Area m\u00b2'] * value['rate']
            result[key] = value

        return result

    def build_boq(self):
        data = self.calculate_rate()
        result = {}

        for key, category_data in data.items():
            category_data.drop(columns=['Calculated Area m\u00b2'], inplace=True)
            category_data.columns = ['category', 'quantity', 'rate', 'cost']
            total = category_data['cost'].sum(axis=0)
            total_row = pd.DataFrame([['total', total, '', '']], columns=['category', 'quantity', 'rate', 'cost'])
            boq = pd.concat([category_data, total_row], axis=0)
            result[key] = boq

        return result




