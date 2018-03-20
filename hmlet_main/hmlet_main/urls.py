from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^scrape/', include('scrape.urls')),
    url(r'^api/', include('api.urls')),
]
