from django.conf.urls import patterns, url

from s2aas import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^sent/$', views.sent, name='sent'),
    url(r'^final/$', views.final, name='final') 
)
