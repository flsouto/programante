# Como calcular o quinto dia útil do mês?
Para calcular o quinto dia útil do mês em Python, você pode criar uma função que itera pelos dias do mês, verifica se cada dia é um dia útil (ignorando fins de semana) e conta quantos dias úteis foram encontrados até atingir o quinto dia útil. Aqui está um exemplo de como você pode fazer isso:

```python
import datetime
import numpy as np

def quinto_dia_util(ano, mes):
    data = datetime.date(ano, mes, 1)
    dias_uteis_encontrados = 0

    while dias_uteis_encontrados < 5:
        if data.weekday() < 5:  # Verifica se é um dia útil (segunda a sexta-feira)
            dias_uteis_encontrados += 1

        data += datetime.timedelta(days=1)  # Avança para o próximo dia

    return data

# Exemplo de uso:
ano_atual = datetime.date.today().year
mes_atual = datetime.date.today().month

quinto_dia = quinto_dia_util(ano_atual, mes_atual)
print(f'O quinto dia útil de {mes_atual}/{ano_atual} é: {quinto_dia.strftime("%d/%m/%Y")}')
```

Neste exemplo, a função `quinto_dia_util` recebe o ano e o mês como argumentos, inicializa uma data no primeiro dia do mês e itera pelos dias até encontrar o quinto dia útil. A verificação de dias úteis é feita utilizando a propriedade `weekday()` da classe `datetime.date`, onde 0 representa segunda-feira e 4 representa sexta-feira. A função retorna a data correspondente ao quinto dia útil do mês.
