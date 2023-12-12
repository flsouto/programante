# Para Que Serve O App.Use Do Express?
O `app.use` no Express.js é uma função que é usada para montar middleware no pipeline de requisições. Middleware são funções que têm acesso ao objeto de requisição (`req`), ao objeto de resposta (`res`) e à próxima função de middleware no ciclo de requisição-resposta do Express (`next`). Essas funções podem realizar tarefas, modificar objetos de requisição e resposta, encerrar o ciclo ou chamar a próxima função de middleware no pipeline.

A assinatura básica da função `app.use` é a seguinte:

```javascript
app.use([path,] callback [, callback, ...])
```

- `path`: É um caminho opcional que especifica um subconjunto de rotas em que o middleware será executado.
- `callback`: É a função de middleware que será executada quando a rota ou caminho correspondente for alcançado.

Por exemplo, se você quiser adicionar um middleware que loga todas as requisições para o console, você pode fazer algo assim:

```javascript
app.use(function(req, res, next) {
  console.log('Recebida uma requisição em: ', new Date());
  next(); // Chama a próxima função de middleware no pipeline
});
```

Se você quiser que o middleware seja executado apenas para um caminho específico, você pode especificar o caminho como o primeiro argumento da função `app.use`:

```javascript
app.use('/admin', function(req, res, next) {
  console.log('Recebida uma requisição em /admin em: ', new Date());
  next();
});
```

Neste exemplo, o middleware só será executado para requisições que tenham como caminho o prefixo "/admin".



