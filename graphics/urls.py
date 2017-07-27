from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.graph, name = 'graph'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^test/$', views.test, name = 'about'),
]
