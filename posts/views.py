from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm


class Lista(View):
	def get(self,request):
		posts = Post.objects.all()
		return render(request,'posts/lista.html',{'posts':posts})


class Detalle(View):
	def get(self,request,id):
		post = Post.objects.get(id=id)
		template_name = 'posts/detalle.html'
		context = {
			'post':post
		}
		return render(request,template_name,context)

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
