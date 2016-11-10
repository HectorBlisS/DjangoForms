from django.conf.urls import url, include
from django.contrib import admin
from posts import urls as postsURLs
from account import urls as accountURL


urlpatterns = [
	url(r'^account/',include(accountURL)),
    url(r'^admin/', admin.site.urls),
    url(r'^',include(postsURLs))
]
