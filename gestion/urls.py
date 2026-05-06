import os
from django.contrib import admin
from django.urls import include, path
from django.conf import settings # Importación correcta
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mascotas.urls')),
]

# Solo añadimos esto una vez, con la condición de que estemos en local o en Render
if settings.DEBUG or os.environ.get('RENDER'):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)