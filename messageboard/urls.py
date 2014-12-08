from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^login/$', views.sign_in, name="sign-in"),
    url(r'^$', views.index, name = 'main'),
    url(r'^logout/$', views.logout_view, name = 'logout'),
    url(r'^new_topic/$', views.new_topic, name='new-topic')
)
