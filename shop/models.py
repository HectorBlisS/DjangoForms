from django.db import models


class Producto(models.Model):
	nombre = models.CharField(max_length=140)
	desc = models.TextField()
	precio = models.CharField(max_length=10)
	img = models.ImageField(blank=True,null=True)

	def __str__(self):
		return self.nombre