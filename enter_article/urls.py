

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cs/$', views.cs),

    url(r'^$',views.show),
    url(r'^show/all/$', views.show),  # 全部文章显示
    url(r'^show/person/$', views.show_person),  # 个人全部文章显示
    url(r'^show/wzxq/(\d+)$', views.show_wzxq),  #文章详情展示
    # url(r'^post/gt$', views.post_gt), # 发布跟帖
    url(r'^wzfb/qbj/$', views.post_article_qbj),
    url(r'^wzfb/$', views.post_article), # 发表文章
]