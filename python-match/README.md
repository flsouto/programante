# Como implementaar Match do PHP no Python?

A função match no PHP 8 é uma função que permite fazer comparações complexas em uma única expressão, semelhante a uma instrução switch. Ela foi introduzida para melhorar a legibilidade e a facilidade de uso em comparações de valores múltiplos. Embora outras linguagens de programação tenham construções semelhantes, o nome e a sintaxe exata podem variar de uma linguagem para outra. Vou destacar algumas linguagens que possuem funcionalidades semelhantes:

## Python

No Python, você pode usar um dicionário (dictionary) para criar um mapeamento de valores para funções ou expressões. Isso é semelhante a um "match" do PHP. Por exemplo:

```python
def match_example(value):
    return {
        'a': 'Valor é a',
        'b': 'Valor é b',
        'c': 'Valor é c',
    }.get(value, 'Valor não encontrado')


if __name__ == "__main__" :
    print(match_example('a'))

```
