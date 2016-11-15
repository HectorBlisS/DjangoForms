from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	GIROS = (
			('tecnologia','Tecnología'),
			('alimentos','Alimentos'),
			('transporte','Transporte'),
			('agricola','Agricola'),
			('educacion','Educación')
		)

	empresa = models.CharField(max_length=140,blank=True,null=True)
	telefono = models.CharField(max_length=14,blank=True,null=True)
	desc = models.TextField(blank=True,null=True)
	img = models.ImageField(blank=True,null=True)
	logo = models.ImageField(blank=True,null=True)
	giro = models.CharField(max_length=140,choices=GIROS,default='tecnologia')
	pagina = models.URLField(blank=True,null=True)
	usuario = models.OneToOneField(User)

	def __str__(self):
		return "El perfil de {}".format(self.usuario)
