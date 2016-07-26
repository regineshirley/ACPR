from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^helmets/', include('helmets.urls')),
    url(r'^swords/', include('swords.urls')),
    url(r'^armor/', include('armor.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^cart/', include('cart.urls'))
]
