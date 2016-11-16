from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^hostname/(?P<hostname_id>\w+)/$', views.hostname_query, name='hostname')
]
