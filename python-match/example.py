def match_example(value):
    return {
        'a': 'Valor é a',
        'b': 'Valor é b',
        'c': 'Valor é c',
    }.get(value, 'Valor não encontrado')


if __name__ == "__main__" :
    print(match_example('a'))
