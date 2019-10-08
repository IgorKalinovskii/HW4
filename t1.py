def lala (lines = 3, la_per_line= 3, end = 0):
    """Пишем функцию, которая генерирует песню la-la-la. Функция принимает 3 аргумента:
1-е число – сколько строк будет в песне. По умолчанию 3
2-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
3-е число – если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце
стоит «!». По умолчанию 0"""
    la = 'la'
    sep = '-'
    count = 0
    output = ''

    while count < lines:
        output += (la + sep) * la_per_line
        output = output[:len(output) - 1] #удаляем последний символ "-" в строке
        output += "\n"
        count += 1

    output = output[:len(output) - 1] #удаляем последний перенос строки

    if end == 0:
        output += "."
    elif end == 1:
        output += '!'

    return output


if __name__ == '__main__':
    print(lala (3,3,0))
    print(lala (18,31,1))




