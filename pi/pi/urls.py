from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^rasp/', include('rasp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('rasp.urls'))
]


