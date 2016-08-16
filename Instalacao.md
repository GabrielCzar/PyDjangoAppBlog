# Instalação

## Instale o pip

	sudo apt install pip

## Crie o diretorio para armazenar o site e entre nele

	mkdir nomeProjeto
	cd nomeProjeto

## Instale o ambiente virtual

	python3 -m venv myvenv

## Ative o ambiente
	
	source myvenv/bin/activate

## Instale o Django no diretorio

	pip install django==1.8.5

- Obs.: Se necessario atualize com 
		
		pip install --upgrade pip

## Crie um projeto
	
	django-admin startproject mysite . 

- obs.: mysite é o nome do projeto nesse contexto

## Faça algumas configurações basicas
- Va em settings.py
	- Altere a TIME_ZONE = 'UTF' para sua localidade se desejar, por exemplo:

			TIME_ZONE = 'America/Fortaleza'

	- Desca ate o final do arquivo e ensira

			STATIC_ROOT = os.path.join(BASE_DIR, 'static') 

## Execute as migrações do banco de dados(banco de dados padrao sera o sqlite3)
	
	python manage.py migrate

## Execute o arquivo com as configurações
	
	python manage.py runserver
	
## Criando uma aplicacao
- Obs.: Pare o server antes de fazer essa mudanças
	
		python manage.py startapp nomeAplicacao

## Faça mais algumas configurações
- Va em settings.py e encontre o code abaixo
 
		INSTALLED_APPS = (   	
		    'django.contrib.admin',  
		    'django.contrib.auth',  
		    'django.contrib.contenttypes',  
		    'django.contrib.sessions',  
		    'django.contrib.messages',  
		    'django.contrib.staticfiles',  
		    'nomeAplicacao', # Voce deve adicionar o nome da aplicacao aqui!  
		)

## Agora so contruir sua aplicação

* ### Para mais informações sobre o Django acesse o repositorio do [Django no Github](https://github.com/django/django.git) ou baixe o respositorio pelos comando do git

		git clone git://github.com/django/django.git
		
