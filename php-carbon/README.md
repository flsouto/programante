# Usando Carbon para calcular idade no PHP

Carbon é uma popular biblioteca de manipulação de datas e horas para PHP que estende a funcionalidade da classe `DateTime`. Vamos usar o Carbon para calcular a diferença de idade entre duas datas, em vez de usar a classe `DateTime`. Certifique-se de ter a biblioteca Carbon instalada para usar este exemplo. Você pode instalá-la via Composer.

Aqui está um exemplo de como usar Carbon para calcular a idade de uma pessoa com base em sua data de nascimento:

```php
require 'vendor/autoload.php';

use Carbon\Carbon;

function calcularIdade($dataNascimento) {
    // Crie um objeto Carbon com a data de nascimento
    $dataNascimento = Carbon::parse($dataNascimento);

    // Crie um objeto Carbon representando a data atual
    $dataAtual = Carbon::now();

    // Calcule a diferença entre as duas datas
    $idade = $dataNascimento->diffInYears($dataAtual);

    return $idade;
}

// Exemplo de uso
$dataNascimento = "1990-05-15";
$idade = calcularIdade($dataNascimento);
echo "A idade é $idade anos.";
```

Neste exemplo, usamos Carbon para criar objetos de data e hora, e os métodos específicos do Carbon, como `parse()` para analisar a data de nascimento, `now()` para obter a data atual e `diffInYears()` para calcular a diferença de idade em anos.

O uso do Carbon torna o código mais legível e fornece uma série de métodos convenientes para trabalhar com datas e horas, facilitando tarefas comuns de manipulação de datas. É uma escolha popular em muitos projetos PHP devido à sua funcionalidade adicional e simplicidade de uso em comparação com a classe `DateTime` nativa do PHP.
