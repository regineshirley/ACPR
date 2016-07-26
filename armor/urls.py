from django.conf.urls import url
from . import views

app_name = 'armor'

urlpatterns = [
    url(r'^$', views.armorview, name='armorview'),
    url(r'^(?P<armor_id>[0-9]+)/$', views.detail, name='detail')
]