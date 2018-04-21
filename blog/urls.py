from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^home/$', views.home, name="home"),
    url(r'^about/$', views.about, name="about"),
    url(r'^socialmedia/$', views.socialmedia, name="socialmedia"),
]
