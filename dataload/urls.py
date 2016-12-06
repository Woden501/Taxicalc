from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^fareinfo/(?P<fare_info_id>[0-9]+)/$', views.load_fare_info, name='fare_info'),
    url(r'^(?P<taxi_fare_id>[0-9]+)/$', views.load_taxi_fare, name='taxi_fare'),
    url(r'^load/$', views.load, name="load"),
]