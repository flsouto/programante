# Como Criar Decorators?
Em TypeScript, você pode criar decorators para modificar ou estender classes e membros de classe. Decorators são funções especiais que podem ser aplicadas a classes, métodos, propriedades e acessadores. Aqui está um exemplo básico de como criar e usar um decorator em TypeScript:

```typescript
// Exemplo de decorator de método simples
function logDecorator(target: any, key: string, descriptor: PropertyDescriptor) {
    const originalMethod = descriptor.value;

    descriptor.value = function (...args: any[]) {
        console.log(`Método ${key} chamado com argumentos: ${JSON.stringify(args)}`);
        const result = originalMethod.apply(this, args);
        console.log(`Resultado: ${result}`);
        return result;
    };

    return descriptor;
}

class MinhaClasse {
    @logDecorator
    soma(a: number, b: number): number {
        return a + b;
    }
}

const instancia = new MinhaClasse();
instancia.soma(2, 3);
```

Neste exemplo, `logDecorator` é um decorator de método simples que loga os argumentos e o resultado do método. Ele é aplicado ao método `soma` da classe `MinhaClasse` usando a sintaxe `@logDecorator`.

A assinatura de um decorator de método é definida como uma função que recebe três parâmetros:
1. `target`: A instância da classe para um método de instância ou o construtor da classe para um método estático.
2. `key`: O nome do método.
3. `descriptor`: Um objeto que contém informações sobre o método.

Dentro do decorator, você pode realizar qualquer lógica desejada antes ou depois da execução do método original. Neste caso, o decorator loga informações antes e depois da chamada do método.
