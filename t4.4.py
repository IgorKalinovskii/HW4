import t3


list1 = ['123123','alskdjlkadlkasd', ['123123','asda'],'asdasdasdasd',
         '\n\t\r9009090990------asdasd@!@#!@#@!##STRINGstring}A{SD}{AS}{D}AS{D}{']

list2 = [t3.clear(n) for n in list1 if type(n) == str]

print(list2)

