# Como Encodar Uma String Em Base64?
Em Node.js, você pode usar a função `Buffer` para codificar uma string em base64. Aqui está um exemplo simples:

```javascript
// Importando o módulo 'buffer'
const buffer = require('buffer');

// String que você deseja codificar em base64
const minhaString = 'Olá, Mundo!';

// Codificando a string em base64
const stringCodificadaBase64 = Buffer.from(minhaString).toString('base64');

console.log('String original:', minhaString);
console.log('String codificada em base64:', stringCodificadaBase64);
```

Neste exemplo, a função `Buffer.from()` converte a string em um objeto Buffer, e então chamamos `.toString('base64')` para obter a representação em base64 dessa string. O resultado é armazenado na variável `stringCodificadaBase64`.
