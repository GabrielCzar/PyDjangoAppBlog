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

	pip install -e django/

## Crie um projeto
	
	django-admin startproject mysite . 

- obs.: mysite é o nome do projeto nesse contexto

# Instruões de Uso

## Ative o ambiente
	
	source myvenv/bin/activate

## Execute o arquivo com as configurações
	
	python manage.py runserver
	

* ### Para mais informações sobre o Django acesse o repositorio do [Django no Github](https://github.com/django/django.git) ou baixe o respositorio pelos comando do git

		git clone git://github.com/django/django.git
		
