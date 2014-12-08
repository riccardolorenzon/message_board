from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^login/$', views.sign_in, name="sign-in"),
    url(r'^$', views.index, name = 'main'),
    url(r'^logout/$', views.logout_view, name = 'logout'),
    url(r'^new_topic/$', views.new_topic, name='new-topic'),
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic_detail, name="topic-detail"),
    url(r'^add_post', views.add_post, name="add-post"),
    url(r'^delete_post/$', views.delete_post, name="delete-post"),
    url(r'^signup/$', views.signup, name="sign-up")

)
