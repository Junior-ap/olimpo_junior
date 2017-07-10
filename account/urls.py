from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': 'account:login'}, name='logout'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^edit/$', views.edit_profile, name='edit_profile'),
]
