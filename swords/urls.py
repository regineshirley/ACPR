from django.conf.urls import url
from . import views

app_name = 'sword'

urlpatterns = [
    url(r'^$', views.swordview, name='swordview'),
    url(r'^(?P<sword_id>[0-9]+)/$', views.detail, name='detail')
]