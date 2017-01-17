from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('database_Send/$', views.database_Send, name='database_Send'),
]
