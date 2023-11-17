# Como utilizar o operador nullsafe no PHP8?

O operador nullsafe (?->) é usado para acessar propriedades ou métodos de objetos em uma cadeia de chamadas, garantindo que, se um dos objetos em qualquer ponto da cadeia for nulo, a expressão retorna nulo, em vez de gerar um erro de chamada em um valor nulo. Isso pode simplificar o código e torná-lo mais seguro quando você trabalha com objetos aninhados que podem ou não estar definidos. Aqui está um exemplo de uso do operador nullsafe em PHP 8:

```php
class Pessoa {
    public function getEndereco() {
        return new Endereco('Rua Principal');
    }
}

class Endereco {
    public function getRua() {
        return 'Rua: ' . $this->rua;
    }
}

// Exemplo sem null-safe operator
$pessoa = new Pessoa();

// Antes do PHP 8.0, seria necessário verificar cada nível da cadeia
if ($pessoa !== null && $pessoa->getEndereco() !== null && $pessoa->getEndereco()->getRua() !== null) {
    echo $pessoa->getEndereco()->getRua();
} else {
    echo 'Rua indisponível';
}

// Exemplo com null-safe operator (PHP 8.0+)
echo $pessoa?->getEndereco()?->getRua() ?? 'Rua indisponível';

```
Suponha que você esteja trabalhando com um objeto Customer que possui uma propriedade address, que por sua vez possui uma propriedade city. No entanto, a propriedade address ou city pode ser nula em alguns casos. Veja como o operador nullsafe pode ser útil:
