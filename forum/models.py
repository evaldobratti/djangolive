from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Label(models.Model):
	nome = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nome

class Categoria(models.Model):
	titulo = models.CharField(max_length=50)
	descricao = models.CharField(max_length=200)
	identificacao = models.CharField(max_length=20)
	categoria_pai = models.ForeignKey("self", blank=True, null=True)

class Topico(models.Model):
	autor = models.ForeignKey(User)
	data_hora_criacao = models.DateTimeField(auto_now_add=True)
	votos = models.IntegerField(blank=True, default=0)
	conteudo = models.CharField(max_length=2000, blank=False)
	labels = models.ManyToManyField(Label, blank=True)
	titulo = models.CharField(max_length=100)
	descricao = models.CharField(max_length=200, blank=True)
	categoria = models.ForeignKey(Categoria, blank=True, null=True)

class Post(models.Model):
	autor = models.ForeignKey(User)
	data_hora_criacao = models.DateTimeField(auto_now_add=True)
	votos = models.IntegerField(blank=True, default=0)
	conteudo = models.CharField(max_length=2000)
	topico = models.ForeignKey(Topico)

	def __unicode__(self):
		return self.conteudo


class UsuarioForum(models.Model):
	user = models.OneToOneField(User)
	topicos_acompanhados = models.ManyToManyField(Topico, blank=True)

	def __unicode__(self):
		return self.user.username

