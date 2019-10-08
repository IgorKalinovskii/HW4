import string


def clear(a):
    """ Удаляет с исходной строки все символы, кроме малых и больших букв
    латинского алфавита"""
    s = list(a)
    res = ''
    for el in s:
        if el in string.ascii_lowercase or el in string.ascii_uppercase:
            res += el

    assert res.isalpha() or res == ''

    return res


if __name__ == '__main__':
    print(clear('123aslalskdlKAJLKJALKJ'))
    print(clear('asldkkajsldkaskldLAKSJKLASDL'))
    print(clear('\n\t\r9009090990------asdasd@!@#!@#@!##STRINGstring}A{SD}{AS}{D}AS{D}{'))
    # print(help(clear))

