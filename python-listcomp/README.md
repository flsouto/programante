# Python List Comprehension

List comprehensions são uma ferramenta útil em Python para criar listas de maneira concisa e elegante. Elas podem ser aplicadas a diversos tipos de problemas, incluindo aqueles relacionados a comércio. Vou te mostrar um exemplo de como usar list comprehension para resolver um problema simples relacionado a comércio: calcular o total de vendas de produtos que custam mais de R$ 100,00.

Suponha que você tenha uma lista de vendas, onde cada venda é representada como uma tupla contendo o nome do produto e o preço. Aqui está como você pode usar list comprehension para calcular o total de vendas de produtos caros:


```python
# Lista de vendas (nome do produto, preço)
vendas = [
    ("Produto A", 120.00), 
    ("Produto B", 80.00), 
    ("Produto C", 150.00), 
    ("Produto D", 90.00)
]

# calcular o total de vendas de produtos caros
total_vendas_caras = sum(
    preco for produto, preco in vendas if preco > 100
)

print("Total: R$", total_vendas_caras)
```

Neste exemplo, a list comprehension é usada para filtrar as vendas com preços maiores que R$ 100 e, em seguida, a função sum() é usada para calcular o total dessas vendas. O resultado será o total de vendas de produtos caros.

Observe que a list comprehension é uma maneira concisa e legível de realizar essa tarefa, tornando o código mais eficiente e fácil de entender.
