# Votação Proz
Sistema de votação para melhor grupo apresentado na matéria de Experiência de Usuários

![alt text](https://github.com/pedrorafante/votacao-proz/blob/main/img/Desenho%20inicial.jpeg?raw=true)

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

