# Como implementar __call do PHP no Python?

Em PHP, a função `__call` é usada para interceptar chamadas a métodos que não são acessíveis ou não existem em uma classe. Em Python, você pode obter um comportamento semelhante usando o método `__getattr__`. Aqui está um exemplo simples que demonstra como você pode implementar algo semelhante ao `__call` do PHP em Python:

```python
class Exemplo:
    def __getattr__(self, nome_do_metodo):
        def metodo_nao_encontrado(*args, **kwargs):
            print(f"Método {nome_do_metodo} não encontrado.")
        
        return metodo_nao_encontrado

# Exemplo de uso
objeto = Exemplo()

# Chama um método que não existe
objeto.metodo_inexistente()  # Saída: Método metodo_inexistente não encontrado.
```

Neste exemplo, a classe `Exemplo` define o método `__getattr__`, que é chamado quando um atributo (método, no caso) não é encontrado no objeto. O método `__getattr__` retorna uma função que imprime uma mensagem indicando que o método não foi encontrado.

