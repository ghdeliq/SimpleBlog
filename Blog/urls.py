"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.views.static import  serve
from django.conf.urls.static import  static
import enter_user
import enter_photo
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^shouye/$', views.shouye),
    url(r'^pp/$', views.pp),
    url(r'^zpq/$', views.zpq),
    url(r'^pi/$', views.pi),
    url(r'^passage/$', views.passage),
    url(r'^enter_user/', include('enter_user.urls', namespace='enter_user', app_name='enter_user')),
    url(r'^enter_article/', include('enter_article.urls', namespace='enter_article', app_name='enter_article')),
    url(r'^enter_photo/', include('enter_photo.urls', namespace='enter_photo', app_name='enter_photo')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    #url(r'^ueditor/',include('DjangoUeditor.urls' )),
] #+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
