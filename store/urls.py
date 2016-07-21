from django.conf.urls import url
from . import views

app_name = 'store'

urlpatterns = [
    #/store/
    url(r'^$', views.index, name='index'),

    #/store/product_id
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),

    # /store/product_id/purchase/
    url(r'^(?P<product_id>[0-9]+)/purchase/$', views.purchase, name='purchase'),

    # /store/product_id/purchase/cart/
    url(r'^(?P<product_id>[0-9]+)/purchase/cart$', views.cart, name='cart')
]