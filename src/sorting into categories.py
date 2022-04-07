import pandas as pd

file = pd.read_csv('C:/Users/bronwen.barratt/Desktop/Hackathon/min_sizes_test.csv')
# print(file)
def sort_categories(width, height):
    maximum = max(width,height)
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

file['category'] = file.apply(lambda x: sort_categories(x['min_width'], x['min_height']), axis=1)
# print(file)

result_categories = file[['Area', 'category', 'Count']].groupby(['category']).sum()
print(result_categories.reset_index())
result_categories.reset_index(inplace=True)

rate = {1:1, 2:2.5, 3:4, 4:5, 5:6}
result_categories['rate'] = result_categories['category'].map(rate)
result_categories['cost'] = result_categories['Area'] * result_categories['rate']
print(result_categories)

total = result_categories['cost'].sum(axis=0)
print("total,",total)