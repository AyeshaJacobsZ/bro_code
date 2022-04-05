def sort_categories(width, height):
    maximum = max(width,height) #convert to int if not already
    addition = width + height
    if maximum < 750 and addition <= 1150:
        category = 'category_1'
    elif maximum < 750 and addition > 1150:
        category = 'category_2'
    elif 750 <= maximum < 1350:
        category = 'category_3'
    elif 1350 <= maximum < 2100:
        category = 'category_4'
    elif 2100 <= maximum:
        category = 'category_5'
    print(category)