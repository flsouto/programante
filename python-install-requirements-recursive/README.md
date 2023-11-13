# Como instalar dependências recursivamente em Python?

Infelizmente, o `pip` não suporta diretamente wildcards para instalar automaticamente dependências de todos os subdiretórios. No entanto, você pode usar algumas estratégias alternativas.

Uma abordagem possível seria criar um script Python ou usar uma ferramenta de gerenciamento de pacotes que suporte instalação recursiva. Aqui está um exemplo de como você pode fazer isso usando Python:

1. Crie um script Python, por exemplo, `install_dependencies.py`, no diretório raiz do seu projeto.
   
```python
# install_dependencies.py

import os
import subprocess

def install_dependencies(directory):
    for root, dirs, files in os.walk(directory):
        if "requirements.txt" in files:
            requirements_path = os.path.join(root, "requirements.txt")
            subprocess.call(["pip", "install", "-r", requirements_path])

if __name__ == "__main__":
    install_dependencies(".")
```

2. Execute o script para instalar as dependências.

```bash
python install_dependencies.py
```

Este script Python percorre recursivamente todos os subdiretórios do diretório atual em busca de arquivos `requirements.txt` e os instala usando o `pip`.

Lembre-se de que esta abordagem assume que todos os seus submódulos têm arquivos `requirements.txt` definidos da mesma maneira.
