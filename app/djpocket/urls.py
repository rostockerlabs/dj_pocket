from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
