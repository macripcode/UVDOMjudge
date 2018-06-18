from django.conf.urls import url
from period.api import views
from course.api.views import filter_period


urlpatterns = [
    url(r'^$', views.periods),
    url(r'^(?P<pk>\d{6})/$', views.period_detail),
]
