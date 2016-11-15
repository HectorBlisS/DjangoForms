from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post, Comentario
from .forms import PostForm, ComentForm

from .mailing import template_email

class Lista(View):
	def get(self,request):
		posts = Post.objects.all()
		return render(request,'posts/lista.html',{'posts':posts})


# class Detalle(View):
# 	def get(self,request,id):
# 		post = Post.objects.get(id=id)

# 		comentarios = Comentario.objects.all().filter(post=post)

# 		template_name = 'posts/detalle.html'
# 		context = {
# 			'post':post,
# 			'comentarios':comentarios
# 		}
# 		return render(request,template_name,context)

class Detalle(View):
	def get(self,request,id):
		post = Post.objects.get(id=id)
		template_name = 'posts/detalle.html'
		form = ComentForm()
		context = {
			'post':post,
			'form':form
		}
		return render(request,template_name,context)

	def post(self,request,id):
		post = Post.objects.get(id=id)
		form = ComentForm(request.POST)
		if form.is_valid():
			nuevo_comen = form.save(commit=False)
			nuevo_comen.autor = request.user
			nuevo_comen.post = post
			nuevo_comen.save()
			return redirect('detalle',id=id)
		return redirect('lista')

class NuevoPost(View):
	def get(self,request):
		template_name = 'posts/nuevo.html'
		form = PostForm()
		context = {
		'form':form
		}
		return render(request,template_name,context)

	def post(self,request):
		template_name = 'posts/nuevo.html'
		form = PostForm(request.POST)
		if form.is_valid():
			nuevo_post = form.save(commit=False)
			nuevo_post.autor = request.user
			nuevo_post.save()
			return redirect('lista')
		context = {
		'form':form
		}
		return render(request,template_name,context)




class Mail(View):
	def post(self,request):
		link = request.POST.get('link')
		amigo = request.POST.get('amigo')
		dic = {
			'titulo':"Titulo de Prueba",
			'mensaje':link,
			'asunto':"el asunto",
			'para':["contacto@fixter.org",amigo]
		}
		template_email(dic)
		return redirect('lista')














