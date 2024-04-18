from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class fotografria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'Fotografia [nome={self.nome}]'
    
class Grupo(models.Model):
    group_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = RichTextField(null=False, blank=False)
    criador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    activity_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = RichTextField(null=False, blank=False)
    data_entrega = models.DateField(null=False, blank=False)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return f'Atividade [titulo={self.titulo}]'