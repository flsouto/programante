# Como verificar se um arquivo existe num bucket da s3 usando Node.js?

Para verificar se um arquivo existe em um bucket da Amazon S3 usando Node.js, você pode utilizar a biblioteca AWS SDK for JavaScript, também conhecida como `aws-sdk`. Certifique-se de instalá-la antes de começar, usando o seguinte comando:

```bash
npm install aws-sdk
```

Aqui está um exemplo de código para verificar a existência de um arquivo em um bucket S3:

```javascript
const AWS = require('aws-sdk');

// Configurar as credenciais da AWS
AWS.config.update({
  accessKeyId: 'SUA_ACCESS_KEY',
  secretAccessKey: 'SUA_SECRET_KEY',
  region: 'SUA_REGIAO', // Por exemplo, 'us-east-1'
});

// Criar um objeto S3
const s3 = new AWS.S3();

// Definir o nome do bucket e o caminho do arquivo
const bucketName = 'NOME_DO_BUCKET';
const key = 'CAMINHO/DO/ARQUIVO.txt';

// Configurar os parâmetros para a operação headObject
const params = {
  Bucket: bucketName,
  Key: key,
};

// Verificar a existência do arquivo
s3.headObject(params, function (err, metadata) {
  if (err && err.code === 'NotFound') {
    console.log('O arquivo não existe.');
  } else if (err) {
    console.log('Erro ao verificar a existência do arquivo:', err);
  } else {
    console.log('O arquivo existe.', metadata);
  }
});
```

Lembre-se de substituir `'SUA_ACCESS_KEY'`, `'SUA_SECRET_KEY'`, `'SUA_REGIAO'`, `'NOME_DO_BUCKET'`, e `'CAMINHO/DO/ARQUIVO.txt'` pelos seus valores reais.

Este código utiliza a operação `headObject` da API da AWS S3 para obter informações sobre o objeto (metadados) sem recuperar o corpo do arquivo. Se o arquivo não existir, a função de callback será chamada com um erro contendo o código `'NotFound'`.
