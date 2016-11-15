from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.views.generic import View, TemplateView

#importamos el decorador para restringir el acceso
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




class Register(View):
	def get(self,request):
		form = UserRegistrationForm()
		template_name = 'account/nuevo_usuario.html'
		context = {
			'form':form
		}
		return render(request,template_name,context)

	def post(self,request):
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			return redirect('login')
		template_name="account/nuevo_usuario.html"
		context = {
			'form':form
		}
		return render(request,template_name,context)


class Perfil(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = "account/perfil.html"
		return render(request,template_name)


