from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^recent/$', views.recent, name='recent'),
    url(r'^$', views.index, name='index')
]