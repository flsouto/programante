# Como fazer crop de uma imagem?
Para cortar (cropar) uma imagem em Python, você pode usar a biblioteca PIL (Pillow). Se você ainda não tiver a biblioteca instalada, você pode instalá-la usando o seguinte comando:

```bash
pip install Pillow
```

Aqui está um exemplo simples de como fazer o crop de uma imagem:

```python
from PIL import Image

def crop_image(input_path, output_path, left, top, right, bottom):
    # Abre a imagem
    original_image = Image.open(input_path)

    # Corta a imagem usando as coordenadas fornecidas
    cropped_image = original_image.crop((left, top, right, bottom))

    # Salva a imagem cortada
    cropped_image.save(output_path)

# Exemplo de uso
input_path = "caminho/para/sua/imagem.jpg"
output_path = "caminho/para/imagem_cortada.jpg"

# Coordenadas do retângulo de crop (left, top, right, bottom)
crop_coordinates = (100, 50, 300, 250)

# Chama a função para cortar a imagem
crop_image(input_path, output_path, *crop_coordinates)
```

Certifique-se de substituir "caminho/para/sua/imagem.jpg" pelo caminho real da sua imagem e ajustar as coordenadas do retângulo de crop conforme necessário.

O método `crop` da classe `Image` da Pillow recebe uma tupla de quatro valores que representam as coordenadas do retângulo a ser cortado na imagem (left, top, right, bottom). O código acima corta a imagem do ponto (100, 50) ao ponto (300, 250).
