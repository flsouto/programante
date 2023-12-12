# Como Fazer Streaming De Arquivo Usando Laravel?
O Laravel facilita o streaming de arquivos usando a classe `StreamedResponse`. Essa classe permite que você envie conteúdo de forma eficiente sem a necessidade de carregar o arquivo inteiro na memória.

Aqui está um exemplo básico de como você pode usar o `StreamedResponse` para fazer streaming de um arquivo em Laravel:

```php
use Illuminate\Support\Facades\Response;

Route::get('/stream/{filename}', function ($filename) {
    // Caminho completo para o arquivo que você deseja fazer streaming
    $filePath = storage_path('app/' . $filename);

    // Verifica se o arquivo existe
    if (!file_exists($filePath)) {
        abort(404);
    }

    // Abre o arquivo para leitura
    $fileStream = fopen($filePath, 'r');

    // Retorna a StreamedResponse
    return Response::stream(
        function () use ($fileStream) {
            // Envia o conteúdo do arquivo para o navegador em pequenos pedaços
            fpassthru($fileStream);
        },
        200,
        [
            'Content-Type' => mime_content_type($filePath),
            'Content-Length' => filesize($filePath),
            'Content-Disposition' => 'inline; filename="' . $filename . '"',
        ]
    );
});
```

Neste exemplo, você precisa criar uma rota que aceite o nome do arquivo como parâmetro. O código verifica se o arquivo existe, abre-o para leitura e, em seguida, utiliza a classe `StreamedResponse` para fazer streaming do conteúdo do arquivo para o navegador.
