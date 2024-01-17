# Como redimensionar uma imagem?
Você pode redimensionar uma imagem em Python usando a biblioteca Pillow (PIL), que fornece uma variedade de funcionalidades de processamento de imagens. Se você ainda não tiver instalado a biblioteca Pillow, você pode instalá-la usando o seguinte comando:

```bash
pip install Pillow
```

Aqui está um exemplo simples de como redimensionar uma imagem usando o Pillow:

```python
from PIL import Image

def redimensionar_imagem(caminho_entrada, caminho_saida, largura, altura):
    # Abre a imagem usando o Pillow
    imagem = Image.open(caminho_entrada)

    # Redimensiona a imagem
    imagem_redimensionada = imagem.resize((largura, altura))

    # Salva a imagem redimensionada
    imagem_redimensionada.save(caminho_saida)

# Exemplo de uso
caminho_entrada = 'caminho/para/sua/imagem.jpg'
caminho_saida = 'caminho/para/imagem_redimensionada.jpg'
largura_desejada = 300
altura_desejada = 200

redimensionar_imagem(caminho_entrada, caminho_saida, largura_desejada, altura_desejada)
```

Neste exemplo, a função `redimensionar_imagem` recebe o caminho da imagem de entrada, o caminho de saída, a largura desejada e a altura desejada. A imagem é aberta, redimensionada e, em seguida, salva no novo tamanho especificado.

