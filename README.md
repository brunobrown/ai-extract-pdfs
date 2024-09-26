### 1. Clonar o Repositório

Comece clonando o repositório do projeto:

```shell
git clone https://github.com/Saldoo-corp/saldoo_auth.git
```

### 2. Instalar Dependências

Certifique-se de que você possui todas as dependências instaladas.
Use o `poetry` para instalar as dependências necessárias:

```shell
poetry install
```

### 3. Criar um Ambiente Virtual

Crie um ambiente virtual para o desenvolvimento.

[Como criar um ambiente virtual](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment)

```shell
poetry shell
```

### 4. Adicione os PDFs no diretório `files`

### 5. Converter os PDFs

Converter todos os PDFs que estão no diretório `files` em JPGs no diretório `images`

```shell
poetry run python pdfs_to_images.py
```

### 6. Crie suas labels

O utilize o `labelImg` para rotular as imagens e salve no diretório labels.

```shell
poetry run labelImg images classes.txt  
```

### 7. Crie a estrutura de datasets

Com o comando abaixo crie o diretório de dataset movendo todas as imagens e labels:

```shell
poetry run labelImg images classes.txt  
```

### 8. Crie o arquivo dataset.yaml

Crie o arquivo conforme o exemplo abaixo:

```yaml
train: dataset/images/train
val: dataset/images/val

nc: 4  # Número de classes

names: # Nome das classes
  0: cnpj
  1: date
  2: value
  3: barcode

#names: [ # Nome das classes em formato de lista
#  'cnpj',
#  'date',
#  'value',
#  'barcode'
#]
```

### 9. Inicie o treinamento

Para iniciar o treinamento utilize o comando abaixo:

```shell
poetry run python training_model.py
```

### 10. Predicação e extração

Para realizar a predicação das imagens e verificar a extração, utilize o comando abaixo:

```shell
poetry run python extract_data.py
```

> #### Atenção: No script, na linha com o trecho de código mostrado abaixo, deve conter todas as label criadas.
> ```python
>>  classes = ['cnpj', 'value', 'date', 'barcode']
> ```