# Como usar DateTime no PHP

O uso da classe `DateTime` em PHP é bastante comum para lidar com datas e horas, e pode ser aplicado a uma variedade de cenários do mundo real. Aqui está um exemplo prático de como usar a classe `DateTime` para resolver um problema em um cenário real: cálculo da diferença de idade entre duas datas.

Suponha que você tenha a data de nascimento de uma pessoa e deseje calcular a idade com base nessa data até a data atual. Vamos criar uma função que recebe a data de nascimento como entrada e retorna a idade da pessoa usando a classe `DateTime`:

```php
function calcularIdade($dataNascimento) {
    // Crie um objeto DateTime com a data de nascimento
    $dataNascimento = new DateTime($dataNascimento);

    // Crie um objeto DateTime representando a data atual
    $dataAtual = new DateTime();

    // Calcule a diferença entre as duas datas
    $diferenca = $dataNascimento->diff($dataAtual);

    // Acesse o atributo "y" (anos) na diferença
    $idade = $diferenca->y;

    return $idade;
}

// Exemplo de uso
$dataNascimento = "1990-05-15";
$idade = calcularIdade($dataNascimento);
echo "A idade é $idade anos.";
```

Neste exemplo, criamos a função `calcularIdade` que recebe a data de nascimento como entrada. Dentro da função, criamos dois objetos `DateTime`, um representando a data de nascimento e o outro representando a data atual. Em seguida, usamos o método `diff()` para calcular a diferença entre as duas datas, que nos fornece um objeto `DateInterval`. Finalmente, acessamos o atributo "y" desse objeto para obter o número de anos e, assim, a idade da pessoa.

Essa é apenas uma aplicação simples da classe `DateTime`, mas ilustra como você pode usar essa classe para resolver problemas do mundo real relacionados a datas e horas de forma eficaz e legível. A classe `DateTime` fornece muitos métodos úteis para realizar operações com datas, como formatação, comparação e manipulação de datas, tornando-a uma escolha poderosa ao lidar com datas em PHP.
