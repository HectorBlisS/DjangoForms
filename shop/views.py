from django.shortcuts import render
from django.views.generic import View
from .models import Producto

class Tienda(View):
	def get(self,request):
		template_name = "shop/tienda.html"
		context = {
			'productos':Producto.objects.all()
		}
		return render(request,template_name,context)
