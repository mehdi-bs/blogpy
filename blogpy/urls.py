
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import url , include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static('contact/static/',document_root=settings.STATIC_ROOT)