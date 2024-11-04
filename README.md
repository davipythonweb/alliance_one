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

- configs para testar ADMIN DJANGO
admin
admin@contato.com
Admin$5000


#### React

##### estrutura Minima para projeto com Vite + React

_____________________________
- node_modules
- public
- src
    - App.jsx
    - main.jsx
- index.html
- packge.json
- packge-lock.json
- vite.config.js
____________________________



* node-version==20.17.0

* npm-version==10.8.2

* react-version==18.3.1

* vite-version==5.4.1

* criar projeto-web com a ferramenta de build/bundler -> vite
`npm create vite@latest .`
`npm install`
`npm run dev`

* gerar arquivos finais para subir no servidor
`npm run build`


- detro de package.json

- "build": "rm -rf ../backend/dist && vite build && mkdir -p ../backend/dist/static && cp -r dist/assets ../backend/dist/static && cp dist/index.html ../backend/dist && rm -rf dist",

* Explicação===>

- O comando vite build cria a pasta dist com os arquivos gerados.
- mkdir -p ../backend/dist/static cria a pasta static dentro do backend, onde os arquivos JavaScript e CSS serão colocados.
- cp -r dist/assets ../backend/dist/static copia a pasta assets para dentro de static.
- cp dist/index.html ../backend/dist copia o index.html para a pasta dist do backend.
- rm -rf dist remove a pasta temporária dist após a cópia.
