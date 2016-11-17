from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$',
		views.Tienda.as_view(),
		name="tienda"),
]