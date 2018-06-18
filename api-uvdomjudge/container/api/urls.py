from django.conf.urls import url
from container.api import views


urlpatterns = [
    url(r'^$', views.containers),
    url(r'^(?P<name_container>\d{12}M\d{2})/$', views.container_detail),
]