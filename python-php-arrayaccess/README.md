# Como implementar ArrayAccess do PHP no Python?

Infelizmente, o conceito de ArrayAccess no PHP não tem uma correspondência direta em Python. O ArrayAccess no PHP é uma interface que permite que um objeto seja acessado como um array, usando notação de colchetes.

Em Python, a abordagem é diferente, pois os objetos podem ser iteráveis e suportar indexação por meio de colchetes, mas não há uma interface específica como o ArrayAccess do PHP.

Se você quiser criar um objeto em Python que se comporte de maneira semelhante ao ArrayAccess do PHP, você pode simplesmente implementar os métodos `__getitem__` e `__setitem__` em sua classe. Aqui está um exemplo simples:

```python
class ArrayLikeObject:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

# Exemplo de uso
obj = ArrayLikeObject()
obj['chave'] = 'valor'
print(obj['chave'])  # Saída: valor
```

Dessa forma, você pode acessar e atribuir valores ao seu objeto usando a notação de colchetes, semelhante ao ArrayAccess no PHP.
