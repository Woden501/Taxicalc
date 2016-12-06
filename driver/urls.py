from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^recent/$', views.recent, name='recent'),
    url(r'^boroughs/$', views.boroughs, name='boroughs'),
    url(r'^borough/average/(?P<borough>\w+)$', views.average_borough_fare, name='borough_average'),
    url(r'^day/$', views.best_day, name='day'),
    url(r'^$', views.index, name='index')
]