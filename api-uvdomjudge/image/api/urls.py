from django.conf.urls import url
from image.api import views


urlpatterns = [
    url(r'^$', views.images),
    url(r'^(?P<pk>\d{1})/$', views.image_detail),
]
