# Desvendando o Nullish Coalescing no TypeScript

Recentemente, o TypeScript introduziu uma funcionalidade poderosa conhecida como "Nullish Coalescing," proporcionando aos desenvolvedores uma maneira concisa e clara de lidar com valores padrão para variáveis nulas ou indefinidas. O nullish coalescing (??) é particularmente útil quando você deseja atribuir um valor padrão apenas se uma variável for nula ou indefinida, em oposição a valores falsos como strings vazias ou zero.

Veja um exemplo:

```typescript
// Utilizando o nullish coalescing para fornecer um valor padrão
const userSettings = {
  theme: 'dark',
  fontSize: 14,
};

const selectedFontSize = userSettings.fontSize ?? 16;

console.log(`Tamanho de Fonte Selecionado: ${selectedFontSize}`);

```

Neste exemplo, a variável selectedFontSize recebe o valor de userSettings.fontSize apenas se userSettings.fontSize não for nulo ou indefinido; caso contrário, ela assume o valor padrão de 16. Essa sintaxe concisa melhora a legibilidade do código e reduz a necessidade de instruções condicionais tradicionais.