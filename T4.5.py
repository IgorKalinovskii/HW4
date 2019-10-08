dict1 = {'name':'Igor', 'surname':'Kalynovskyi', 'age':'32', 'position':'QA', 'address':'some_adress',
         'skills':'python'}
dict2 = {a:type(b) for a, b in dict1.items()}
print(dict2)
