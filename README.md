# Votação Proz
Sistema de votação para melhor grupo apresentado na matéria de Experiência de Usuários


![alt text](https://github.com/pedrorafante/votacao-proz/blob/main/img/Desenho%20inicial.jpeg?raw=true)

>
> **Note**: Montar Ambiente Django
```console
python --version
```
Instalar o Python Version 3.11.0

```console
cd django
```
 
```console
cd pip install -r requirements.txt
```



```console
 virtualenv --version
```
virtualenv 20.23.1 - Caso não tenha instalar 
```console
pip install virtualenv
```


```console
pip install django
```

PASSO A PASSO 

CRIAR UM AMBIENTE VIRTUAL
python -m venv NOME_DO_AMBIENTE

ATIVAR 
NOME_DO_AMBIENTE\Scripts\activate
se der erro pra ativar no windons execute esse comando no powerShell 'Set-Execution Unrestricted -Force'

INSTALE AS Dependências
pip install -r requirements.txt
OU
python.exe -m pip install --upgrade pip
pip install django
pip install django-allauth
pip install python-decouple


Sincronize a base de dados
python .\manage.py migrate 

Crie um usuário (Administrador do sistema)
python .\manage.py createsuperuser 

