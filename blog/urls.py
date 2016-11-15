from django.conf.urls import url, include
from django.contrib import admin
from posts import urls as postsURLs
from accounts import urls as accountURL
from django.views.static import serve
from django.conf import settings



urlpatterns = [
	url(r'^accounts/',include(accountURL)),
    url(r'^admin/', admin.site.urls),
    url(r'^',include(postsURLs)),
    url(
    		regex = r'^media/(?P<path>.*)$',
    		view = serve,
    		kwargs = {'document_root':settings.MEDIA_ROOT}
    	),
    url('',
    	include('social.apps.django_app.urls',
    		namespace='social')),
]
