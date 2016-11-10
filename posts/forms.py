from django import forms
from .models import Post, Comentario


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['titulo','cuerpo']
		labels = {'titulo':'cual es tu pollollon?'}

class ComentForm(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = ['cuerpo']
		labels = {'cuerpo':'Escribe tu comentario'}