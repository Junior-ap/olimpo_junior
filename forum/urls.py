from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.list_topic, name='feed'),
    url(r'^ask/', views.create_topic  , name='ask'),
    url(r'^detail/(?P<pk>\d+)', views.detai_topic, name='detail'),
    url(r'^answers/(?P<pk>\d+)/correct', views.reply_correct, name='reply_correct'),
    url(r'^answers/(?P<pk>\d+)/incorrect', views.reply_incorrect, name='reply_incorrect')
]
