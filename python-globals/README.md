# Para que serve a função globals() em Python?

A função globals() retorna um dicionário que contém todas as variáveis globais disponíveis no escopo atual do programa. Aqui está um exemplo simples de como você pode usá-la:

```python
# Definindo algumas variáveis globais
global_var1 = 42
global_var2 = "Hello, world"

# Função que imprime as variáveis globais usando globals()
def imprimir_variaveis_globais():
    global_vars = globals()
    for var_name, var_value in global_vars.items():
        print(f"{var_name}: {var_value}")

# Chame a função para imprimir as variáveis globais
imprimir_variaveis_globais()
```

Neste exemplo, definimos duas variáveis globais, global_var1 e global_var2, e em seguida, criamos a função imprimir_variaveis_globais() que usa a função globals() para listar e imprimir todas as variáveis globais disponíveis no escopo atual. Quando você chama imprimir_variaveis_globais(), verá a saída que mostra todas as variáveis globais e seus valores:

```
__name__: __main__
__doc__: None
__package__: None
global_var1: 42
global_var2: Hello, world
```

Observe que, além das variáveis que definimos, globals() também inclui outras variáveis especiais relacionadas ao ambiente de execução do programa, como __name__, __doc__, e __package__.
