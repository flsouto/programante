# Como fazer upload de arquivos usando PyDrive?
O PyDrive é uma biblioteca Python que simplifica a interação com a API do Google Drive. Para fazer o upload de um arquivo usando o PyDrive, você precisa seguir alguns passos:

1. **Instalação do PyDrive:**
   Certifique-se de ter o PyDrive instalado. Você pode instalá-lo usando o seguinte comando:

   ```bash
   pip install pydrive
   ```

2. **Configuração da API do Google Drive:**
   Antes de usar o PyDrive, é necessário configurar a API do Google Drive e obter as credenciais. Siga as instruções neste link: [Configurar acesso à API](https://pythonhosted.org/PyDrive/quickstart.html).

3. **Exemplo de código:**
   Aqui está um exemplo básico de como fazer o upload de um arquivo usando o PyDrive:

   ```python
   from pydrive.auth import GoogleAuth
   from pydrive.drive import GoogleDrive

   # Autenticação
   gauth = GoogleAuth()
   gauth.LocalWebserverAuth()  # Cria um servidor local e faz a autenticação interativa.

   # Cria a interface de acesso ao Google Drive
   drive = GoogleDrive(gauth)

   # Caminho local do arquivo que você deseja fazer o upload
   file_path = '/caminho/do/seu/arquivo.txt'

   # Cria um objeto File no Google Drive
   file_drive = drive.CreateFile({'title': 'Nome do Arquivo no Google Drive'})
   
   # Define o arquivo local a ser enviado para o Google Drive
   file_drive.SetContentFile(file_path)

   # Envia o arquivo para o Google Drive
   file_drive.Upload()

   print("Upload concluído!")
   ```

Certifique-se de substituir `/caminho/do/seu/arquivo.txt` pelo caminho local do seu arquivo e `'Nome do Arquivo no Google Drive'` pelo nome que você deseja dar ao arquivo no Google Drive.
