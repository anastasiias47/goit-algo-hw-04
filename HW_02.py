
def get_cats_info(path):
    try:
        with open(path,'r',encoding='utf-8') as cat_info_file:
            cat_data = cat_info_file.read().splitlines()
        print(cat_data)
        cats_info = []
        for cat in cat_data:
            cat = cat.split(',')
            cats_info.append({'id':cat[0],'name':cat[1],'age':cat[2]})
    except FileNotFoundError:
        print("Sorry, there is no such file on the following directory")

get_cats_info('cats_info')

test = {'id':'fdfdosfp','sex':'ps[a]s'}

print(test['id'])
