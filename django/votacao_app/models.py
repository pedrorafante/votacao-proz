from django.db import models
from django.contrib.auth.models import User

class Grupo(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=200,unique=True)
    codigo = models.CharField(max_length=4)
    grupo = models.ForeignKey(Grupo,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.email
    
