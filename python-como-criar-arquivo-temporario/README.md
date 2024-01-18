# Como criar um arquivo temporário?
Em Python, você pode criar um arquivo temporário usando o módulo `tempfile`. O `tempfile` fornece uma maneira conveniente de criar arquivos temporários de forma segura. Aqui está um exemplo simples de como criar um arquivo temporário:

```python
import tempfile

# Cria um arquivo temporário e retorna um objeto de arquivo
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    # 'delete=False' impede a exclusão automática do arquivo ao fechar

    # Use o objeto de arquivo temporário como desejado
    temp_file.write(b"Conteúdo do arquivo temporário")

    # Obtenha o nome do arquivo temporário
    temp_file_path = temp_file.name
    print(f"Nome do arquivo temporário: {temp_file_path}")

# O arquivo temporário será excluído automaticamente ao sair do bloco 'with'
```

Neste exemplo, `NamedTemporaryFile` é usado para criar um arquivo temporário. O parâmetro `delete=False` é especificado para que o arquivo não seja excluído automaticamente ao fechar. O nome do arquivo temporário é acessado através da propriedade `name` do objeto de arquivo temporário.
