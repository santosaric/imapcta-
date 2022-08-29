# cyber-burguer

======================================================================================

Para ter o projeto na maquina faça o Git Clone.
Será necessario criar um Virtual Enviroment, para isso rode na raiz do projeto pelo terminal o seguinte comando:

$ pip install virtualenv

Para criar a maquina virtual:

$ virtualenv venv(ou o nome que vc queira dar pra maquina virtual)

Para ativar a maquina virtual:

$ source venv(ou o nome que deu)/bin/activate

======================================================================================

Agora instale as dependecias:

$ pip install django whitenoise gunicorn django-bootstrap4 psycopg2-binary django-stdimage

======================================================================================

Agora com tudo instalado para rodar o projeto e acessar o admin localmente digite:

$ python3 manage.py runserver

Após esse processo se der tudo certo aparecera uma mensagem como esta:

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

August 29, 2022 - 19:59:03

Django version 4.1, using settings 'cyberburguer.settings'

Starting development server at http://127.0.0.1:8000/ <------------ clique no link e no navegador adicione admin após a barra (ex: http://127.0.0.1:8000/admin/)

Quit the server with CONTROL-C.
