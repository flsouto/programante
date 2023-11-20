# Como armazenar arquivo json no S3 a partir de uma função lambda em Node.js?

Para armazenar um arquivo JSON no Amazon S3 (Simple Storage Service) a partir de uma função Lambda em Node.js, você pode usar a biblioteca AWS SDK for JavaScript no Node.js, que facilita a interação com os serviços da AWS, incluindo o S3. Aqui está um exemplo básico de como você pode fazer isso:

Certifique-se de que você tenha o pacote `aws-sdk` instalado em seu projeto Node.js. Você pode instalá-lo usando o seguinte comando:

```bash
npm install aws-sdk
```

Aqui está um exemplo de código Lambda em Node.js que salva um arquivo JSON no S3:

```javascript
const AWS = require('aws-sdk');

// Configurar as credenciais da AWS
AWS.config.update({
  accessKeyId: 'sua_access_key',
  secretAccessKey: 'seu_secret_key',
  region: 'sua_regiao'
});

const s3 = new AWS.S3();

exports.handler = async (event, context) => {
  // Seu objeto JSON
  const jsonData = {
    key1: 'value1',
    key2: 'value2',
    key3: 'value3'
  };

  // Nome do arquivo no S3
  const fileName = 'exemplo.json';

  // Parâmetros para a operação de upload
  const params = {
    Bucket: 'seu-bucket-s3',
    Key: fileName,
    Body: JSON.stringify(jsonData),
    ContentType: 'application/json'
  };

  try {
    // Realizar o upload do arquivo para o S3
    const result = await s3.upload(params).promise();
    console.log('Arquivo enviado com sucesso:', result.Location);
    return {
      statusCode: 200,
      body: 'Arquivo enviado com sucesso!'
    };
  } catch (error) {
    console.error('Erro ao enviar o arquivo:', error);
    return {
      statusCode: 500,
      body: 'Erro ao enviar o arquivo para o S3.'
    };
  }
};
```

Certifique-se de substituir `'sua_access_key'`, `'seu_secret_key'`, `'sua_regiao'`, e `'seu-bucket-s3'` com suas próprias credenciais e informações de configuração.

Este exemplo assume que você já tenha configurado um bucket no S3 para armazenar os arquivos. Certifique-se de conceder as permissões adequadas à sua função Lambda para acessar o bucket S3.
