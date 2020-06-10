
from django.conf.urls import url
from . import views
from django.conf import settings
from django.views.static import  serve

urlpatterns = [
    url(r'^$', views.index),
    url(r'^zpq/$', views.photo_show), # 照片墙
    url(r'^photo/cs$', views.cs),
    url(r'^zpxq/(\d+)$', views.show_detail), # 照片详情
    #url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]