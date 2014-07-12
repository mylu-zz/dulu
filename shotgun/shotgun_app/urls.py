from django.conf.urls import patterns, url

from shotgun_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^index$', views.create_handler, name='create_handler')

)
