from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^mail/$',views.Mail.as_view(),name="mail"),
	url(r'^new/$', views.NuevoPost.as_view(),name="nuevo"),
	url(r'^(?P<id>\d+)/$',views.Detalle.as_view(),name="detalle"),
	url(r'^$',views.Lista.as_view(),name="lista"),
	
]