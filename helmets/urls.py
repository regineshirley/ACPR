from django.conf.urls import url
from . import views

app_name = 'helmet'

urlpatterns = [
    url(r'^$', views.helmetview, name='helmetview'),
    url(r'^(?P<helmet_id>[0-9]+)/$', views.detail, name='detail')
]