from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    url(r'^uv-domjudge/v1/courses/', include('course.api.urls', namespace='api-course')),
    url(r'^uv-domjudge/v1/containers/', include('container.api.urls', namespace='api-container')),
    url(r'^uv-domjudge/v1/images/', include('image.api.urls', namespace='api-image')),
    url(r'^uv-domjudge/v1/periods/', include('period.api.urls', namespace='api-period')),

    # authenthication
    url(r'^uv-domjudge/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^uv-domjudge/v1/rest-auth/', include('rest_auth.urls')),
    url(r'^uv-domjudge/v1/rest-auth/registration/', include('rest_auth.registration.urls')),

]
