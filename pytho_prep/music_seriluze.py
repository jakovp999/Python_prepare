import json
import pickle

my_favorite_group = {'name': 'aqua', 'tracks':['Roses and Red', 'Barbie Girl'],
'alboms': [{'name': 'Aquarium', 'year':1997}, {'name': 'Aquarius', 'year': 2000}]}

print(my_favorite_group)
print(type(my_favorite_group))

js_group = json.dumps(my_favorite_group)
print(js_group)
print(type(js_group))

pc_group = pickle.dumps(my_favorite_group)
print(pc_group)
print(type(pc_group))

with open('group.json', 'w', encoding = 'utf-8') as f:
    json.dump(my_favorite_group, f)

with open('group.picle', 'wb') as f:
    pickle.dump(my_favorite_group, f)