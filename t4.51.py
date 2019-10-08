import t3


dict1 = {'name': 'Igor', 'surname': 'Kalynovskyi', 'age': 32, 'position':'QA', 'address':'prospekt Svobody 18 kv 119',
         'skills':'python'}
dict2 = {a: t3.clear(b).lower() for a, b in dict1.items() if type(b) == str}

print(dict2)
