# Como inserir uma letra antes de uma sequência de números com regex?
Para inserir uma letra antes de uma sequência de números usando regex em Python, você pode usar a função `re.sub()` do módulo `re`. Aqui está um exemplo básico:

```python
import re

def inserir_letra(match):
    return 'X' + match.group(0)

texto = "12345 67890"
padrao = r'\b\d+\b'

resultado = re.sub(padrao, inserir_letra, texto)

print(resultado)
```

Neste exemplo, o padrão `\b\d+\b` corresponde a uma sequência de dígitos (\d+) entre limites de palavra (\b). A função `inserir_letra` é uma função de substituição que pega a correspondência encontrada (a sequência de números) e adiciona a letra desejada (neste caso, 'X') antes dela.

Este código imprimirá:

```
X12345 X67890
```

