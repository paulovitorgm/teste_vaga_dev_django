# Desafio dev Django

---

### Para reconstruir o ambiente para as páginas


#### Sobre o ambiente

Todo esse projeto é gerenciado pelo Poetry, a versão usada durante o desenvolvimento é `1.8.3`:


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
Na pasta onde o projeto está use os comandos:

```bash
pyenv install 3.12.5
```

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

### Sobre os comandos

Os comandos para executar funções como iniciar servidor local e fomatar nos padrões delimitados no linter de código `taskipy`:


    --list  para listar os comandos disponíveis
    run     inicia o servidor
    lint    verifica se o código tem algum problema de escrita
    format  corrige possíveis falhas de estilo no código
    m       encurta o comando 'python manage.py'
    test    executa os testes


Para executar qualquer comando, basta usar: `task <comando>`, como por exemplo `task run`.


#### Para rodar o projeto use os comandos na ordem (o ambiente virtual deve estar ativo)
```
task m makemigrations
```
```
task m migrate
```
```
task run
```
#### Além disso, crie um arquivo chamado .env
Dentro dele altere a secret key.
Você pode criar uma usando o terminal com o comando (o ambiente virtual deve estar ativo):

``` bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
A chave gerada deve ser copiada para o arquivo .env
    
    Exemplo:

    SECRET_KEY=*jtqr0osvh2^9d-fe44u7^w9m)x=zsf#=#^3z#wo^0(y)m$jb4

##### Para acessar o admin é necessário criar um superusuário
```
task m createsuperuser
```
##### Forneça os dados que serão pedidos:
```username```

```email (opcional)```

```password```



### As rotas disponíveis na aplicação são:
Index:
```
http://127.0.0.1:8000/
```
Cadastrar Tarefa:
```
http://127.0.0.1:8000/tarefas/criar
```
Listar todas as tarefas:
```
http://127.0.0.1:8000/tarefas/lista/
```
Mostar tarefa pelo id:
```bash
http://127.0.0.1:8000/tarefas/lista/<int:tarefa_id>/
```
Cadastrar tempo de trabalho:
```
http://127.0.0.1:8000/tempo/cadastrar/
```
Listar todos os tempos cadastrados:
```
http://127.0.0.1:8000/tempo/lista/
```
Django admin:
```
http://127.0.0.1:8000/admin/
```

Existem links para as rotas disponíveis em todas as páginas.