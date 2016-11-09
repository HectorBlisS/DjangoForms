from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	titulo = models.CharField(max_length=140)
	cuerpo = models.TextField()
	autor = models.ForeignKey(User,related_name='posts')
	fecha = models.DateTimeField(auto_now=True)
	publicado = models.BooleanField(default=False)

	def __str__(self):
		return self.titulo

class Comentario(models.Model):
	cuerpo = models.TextField()
	fecha = models.DateTimeField(auto_now=True)
	autor = models.ForeignKey(User,related_name='comentarios')
	post = models.ForeignKey(Post,related_name='comentarios')

	def __str__(self):
		return "{} comentó en {}".format(self.autor,self.post)


		