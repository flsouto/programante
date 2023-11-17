# Como usar Generics no TypeScript?

Vamos considerar um cenário de comércio eletrônico em que você deseja criar um carrinho de compras genérico em TypeScript. Um carrinho de compras pode conter vários tipos de produtos, como eletrônicos, roupas, alimentos, etc. Você pode usar generics para criar um carrinho de compras que seja flexível o suficiente para lidar com diferentes tipos de produtos.

Aqui está um exemplo simplificado:

```typescript
class CarrinhoDeCompras<T> {
  private itens: T[] = [];

  adicionarItem(item: T) {
    this.itens.push(item);
  }

  removerItem(item: T) {
    const index = this.itens.indexOf(item);
    if (index !== -1) {
      this.itens.splice(index, 1);
    }
  }

  listarItens(): T[] {
    return this.itens;
  }
}

// Exemplos de uso

// Carrinho para produtos eletrônicos
const carrinhoEletronicos = new CarrinhoDeCompras<string>();
carrinhoEletronicos.adicionarItem("Smartphone");
carrinhoEletronicos.adicionarItem("Laptop");

// Saída: ["Smartphone", "Laptop"]
console.log(carrinhoEletronicos.listarItens()); 

// Carrinho para produtos alimentícios
const carrinhoAlimentos = new CarrinhoDeCompras<number>();
carrinhoAlimentos.adicionarItem(2);
carrinhoAlimentos.adicionarItem(3);

// Saída: [2, 3]
console.log(carrinhoAlimentos.listarItens());

```

Neste exemplo, a classe CarrinhoDeCompras utiliza um tipo genérico T para representar o tipo de itens que podem ser adicionados ao carrinho. Isso permite que o carrinho de compras seja usado para produtos de diferentes tipos, como strings (eletrônicos) e números (alimentos). Dessa forma, você pode criar um carrinho de compras flexível que é tipado de acordo com o tipo de produto que está manipulando. Isso é útil em um cenário de comércio eletrônico, onde você lida com vários tipos de produtos.
