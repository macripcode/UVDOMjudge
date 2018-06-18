from django.conf.urls import url
from course.api import views


urlpatterns = [
    url(r'^$', views.courses),
    url(r'^(?P<pk>\d{12}M\d{2})/$', views.course_detail),
    url(r'^(?P<id_academic_period>\d{6})/periods/$', views.filter_period),
    url(r'^(?P<id_professor>[0-9]+)/professor/$', views.filter_professor),
    url(r'^(?P<id_signature>[0-9]+)/signature/$', views.filter_signature),
]
