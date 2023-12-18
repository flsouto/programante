# como usar regex para extrair textos entre parênteses?
Para extrair texto entre parênteses usando expressões regulares (regex) em Python, você pode usar o módulo `re`. Aqui está um exemplo simples que mostra como fazer isso:

```python
import re

# Texto de exemplo
texto = "Isso é um (exemplo) de como extrair (textos) entre parênteses."

# Padrão de expressão regular para encontrar texto entre parênteses
padrao = r'\((.*?)\)'

# Aplicar o padrão ao texto usando re.findall
resultados = re.findall(padrao, texto)

# Imprimir os resultados
for resultado in resultados:
    print(resultado)
```

Neste exemplo, o padrão `r'\((.*?)\)'` é usado. Aqui está uma explicação do padrão:

- `\(`: Corresponde ao caractere de abertura de parêntese "(".
- `(.*?)`: É um grupo de captura não ganancioso que corresponde a qualquer sequência de caracteres (exceto uma nova linha) entre parênteses. O `?` torna a correspondência não gananciosa, garantindo que ela pare assim que encontrar o primeiro parêntese de fechamento ")".
- `\)`: Corresponde ao caractere de fechamento de parêntese ")".

A função `re.findall` é usada para encontrar todas as correspondências do padrão no texto. Os resultados são retornados como uma lista, e o loop `for` é usado para imprimir cada correspondência encontrada.

Adapte o código conforme necessário para o seu caso específico.
