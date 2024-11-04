# alliance_one
Aplicação com Django e Django-Rest-Framework + React



### Django

 `Fluxo do Django Framework`

  ![Fluxo-Django](https://github.com/davipythonweb/praticing_django_/blob/main/django-architecture.webp?raw=true)

  - instalar pacote
  pip install + nome do pacote
- fazer os testes
  python manage.py test



ˋcomandos djangoˋ

- criado projeto
  django-admin startproject core .
- rodar projeto
  python manage.py runserver
- criando app
  python manage.py startapp + nome
- criar as tabelas no banco
  python manage.py migrate
- fazendo mudancas e criar os arquivos de migracoes
  python manage.py makemigrations
- criando super usuario admin
  python manage.py createsuperuser user>admin



- migrando para banco PostgreSQL
`comandos`
`acessar shell postgres (windows)`
- psql -U postgres
`lista todos os bancos`
- \l
`criar banco`
- CREATE DATABASE (nome do banco);
`sair`
- \q
`drive para django e postgres`
- pip install psycopg2
`para usar variaveis de ambient`
- pip install python-dotenv


#### 

