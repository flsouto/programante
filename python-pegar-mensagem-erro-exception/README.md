# como pegar a mensagem de erro de um exception?
Em Python, você pode obter a mensagem de erro de uma exceção usando a cláusula `except` juntamente com a variável que armazena a instância da exceção. Essa variável é frequentemente chamada de `e` (poderia ser qualquer nome válido).

Aqui está um exemplo:

```python
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except Exception as e:
    # Captura a exceção e imprime a mensagem de erro
    print(f"Ocorreu uma exceção: {e}")
```

No exemplo acima, a divisão por zero gera uma exceção do tipo `ZeroDivisionError`. A mensagem de erro associada a essa exceção é então acessada através da variável `e`. O bloco `except` é executado, e a mensagem de erro é impressa.

