from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.TextField(max_length=40)


class Exame(models.Model):
    id_exame = models.AutoField(primary_key=True)
    nome_exame = models.TextField()
    data_exame = models.DateField()
    email = models.EmailField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    
