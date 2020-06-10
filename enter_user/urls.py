from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^cs/$', views.cs),
    url(r'^regist/$',views.regist),
    url(r'^login/$',views.login),
    url(r'^logout/$',views.logout),
    url(r'^pp/$', views.pp), # 进入个人主页
    url(r'^person_info/$',views.detail_info),  # 个人信息展示页面
    url(r'^detail_info/jr$', views.detail_info_jr),
    url(r'^xgxx/go/$', views.xgxx_go),  # 去修改个人信息 的页面
    url(r'^xgxx/$',views.Modify1.as_view()),  # 修改个人信息处理逻辑
]