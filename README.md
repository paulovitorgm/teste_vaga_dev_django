# Desafio dev Django

---

### Para reconstruir o ambiente para as páginas

#### Sobre o ambiente

Todo esse projeto é gerenciado pelo Poetry, a versão usada durante o momento da escrita é `1.8.3`:




```
A versão usada do python é 3.12.5
```

```
A versão usada do Django é 5.1.2
```
```
O banco de dados é o SQLite.
```

#### Para configurar todo o ambiente basta executar:

Caso a versão do python instalada no computador seja diferente da 3.12.5:

Instale o pyenv:
```bash
pip install pyenv
```
Na pasta onde o projeto está use o comando:
```bash
pyenv local 3.12.5
```
A seguir:

```bash
pip install poetry==1.8.3
```

Para ativar o ambiente virtual:
```bash
poetry shell
```
Para instalar as dependências:
```bash
poetry install --with dev
```



#### Sobre os comandos

Os comandos para executar funções como iniciar servidor local e fomatar nos padrões delimitados no linter de código `taskipy`:

```bash
task    --list
run     inicia o servidor
lint    verifica se o código tem algum problema de escrita
format  corrige possíveis falhas de estilo no código
m       encurta o comando 'python manage.py'
```

Para executar qualquer comando, basta usar: `task <comando>`, como por exemplo `task run`.


#### Para rodar o projeto use os comandos na ordem
```
task m makemigrations
task m migrate
task run
```

##### Para acessar o admin é necessário criar um superusuário
```
task m createsuperuser
```
###### Fornecer os dados que serão pedidos