import json as js

filepath = r'E:\Programmming\python\ML\usd.json'

with open(filepath, 'r') as jsonfile:
    data = js.load(jsonfile)
    
print(data)