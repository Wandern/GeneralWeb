"""GeneralWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets,  routers


# TODO: Begin documentation of API using Sphinx and/or Django Swagger
# User Serialization is fine in the Projects url for the time being, but this should be encapsulated to its own app.
# Serializers define the API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    # mvplanding can be replaced with modules that import mvplanding.
    # Style used for mvplanding page will start out as Bootstrap, but should be simple enough to use
    # Foundation or Yahoo's Pure.
    # TODO: Make online documentation available of how my projects modules interact together.
    # This will be outlined in external programmers documentation.
    url(r'^$', 'newsletter.views.home', name='home'),
    # url(r'^$', 'storefront.views.home', name='home'),
    url(r'^contact/', 'contact.views.contact', name='contact'),
    url(r'^contact/thanks', 'contact.views.thanks', name='thanks'),
    url(r'^about/', 'about.views.about', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# django rest framework api urls defined here.
# TODO: Add api root url as well as group and user information  from admin (django.contrib.auth.models)
urlpatterns += [
    # url(r'^api/users/', include('users.urls')),
    url(r'^api/snippets/', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

