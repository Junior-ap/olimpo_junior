from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.list_topic, name='feed'),
    url(r'^ask/', views.create_topic  , name='ask'),
    url(r'^detail/(?P<pk>\d+)', views.detai_topic, name='detail'),

]
