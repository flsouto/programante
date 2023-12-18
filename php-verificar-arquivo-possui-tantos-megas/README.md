# como verificar se arquivo possui mais que tantos megas?
Você pode usar a função `filesize` para obter o tamanho de um arquivo em bytes e, em seguida, converter esse tamanho para megabytes para realizar a verificação. Aqui está um exemplo simples em PHP:

```php
<?php
$limiteEmMegas = 5; // Defina o limite desejado em megabytes
$arquivoParaVerificar = 'caminho/do/seu/arquivo.ext';

// Obtém o tamanho do arquivo em bytes
$tamanhoEmBytes = filesize($arquivoParaVerificar);

// Converte bytes para megabytes
$tamanhoEmMegas = $tamanhoEmBytes / (1024 * 1024);

// Verifica se o tamanho é maior que o limite
if ($tamanhoEmMegas > $limiteEmMegas) {
    echo 'O arquivo é maior que ' . $limiteEmMegas . ' megabytes.';
} else {
    echo 'O arquivo está dentro do limite de ' . $limiteEmMegas . ' megabytes.';
}
?>
```

Certifique-se de substituir `'caminho/do/seu/arquivo.ext'` pelo caminho real e nome do seu arquivo. O código acima calculará o tamanho do arquivo em megabytes e, em seguida, comparará com o limite definido. Se o tamanho do arquivo for maior que o limite, uma mensagem indicando isso será exibida.
