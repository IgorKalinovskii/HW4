def scnd(*args):
    """Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов.
Учитываем, что может быть повторяющиеся значения аргументов."""
    s = []
    for el in args:
        s.append(el)

    s.sort()
    s1 = []

    for index,el in enumerate(s):
        if not (el == s[index - 1]):
            s1.append(el)

    return s1[1]


if __name__ == '__main__':
    print (scnd(1,1,1,1,3,3,17,17))
