# Como calcular a diferença de dias entre duas datas?
Você pode calcular a diferença de dias entre duas datas em Python utilizando a biblioteca `datetime`. Aqui está um exemplo de como fazer isso:

```python
from datetime import datetime

# Defina as duas datas que você deseja comparar
data1 = datetime(2023, 1, 1)
data2 = datetime(2023, 12, 31)

# Calcule a diferença entre as duas datas
diferenca = data2 - data1

# Acesse o atributo days para obter o número de dias
diferenca_em_dias = diferenca.days

print(f'A diferença em dias entre as duas datas é: {diferenca_em_dias} dias')
```

Neste exemplo, `data1` e `data2` são objetos `datetime` que representam as duas datas que você deseja comparar. Em seguida, a diferença entre essas duas datas é calculada, e o atributo `days` é acessado para obter o número de dias de diferença.

