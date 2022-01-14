import json
import pickle


with open('group.json', 'r', encoding= 'utf-8') as f:
    result = json.load(f)
print(result)
print(type(result))

with open('group.picle', 'rb') as f:
    result = pickle.load(f)
print(result)
print(type(result))