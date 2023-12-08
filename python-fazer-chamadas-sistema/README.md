# Como Fazer Chamadas De Sistema?
Em Python, você pode fazer chamadas de sistema usando o módulo `subprocess`. Este módulo fornece uma maneira de criar processos, conectar-se aos seus pipes de entrada/saída/erro e obter códigos de retorno. Aqui está um exemplo básico:

```python
import subprocess

# Exemplo de chamada de sistema para listar arquivos no diretório atual
resultado = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, text=True)

# Imprime a saída do comando
print(resultado.stdout)

# Verifica o código de retorno
if resultado.returncode == 0:
    print("Comando executado com sucesso")
else:
    print(f"Erro na execução. Código de retorno: {resultado.returncode}")
```

No exemplo acima, o comando `ls -l` é executado, e a saída é capturada em `resultado.stdout`. O código de retorno do processo é armazenado em `resultado.returncode`.

Você também pode usar `subprocess.Popen` para casos mais avançados, como comunicação contínua com o processo ou redirecionamento de entradas e saídas. Aqui está um exemplo básico:

```python
import subprocess

# Exemplo de chamada de sistema usando subprocess.Popen
processo = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE, text=True)

# Obtém a saída do processo
saida, erro = processo.communicate()

# Imprime a saída do comando
print(saida)

# Verifica o código de retorno
if processo.returncode == 0:
    print("Comando executado com sucesso")
else:
    print(f"Erro na execução. Código de retorno: {processo.returncode}")
```


