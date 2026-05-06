from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_mascotas, name='lista_mascotas'),
    path('crear/', views.crear_mascota, name='crear_mascota'),
    path('editar/<int:id>/', views.editar_mascota, name='editar_mascota'),
    path('eliminar/<int:id>/', views.eliminar_mascota, name='eliminar_mascota'),
    path('duenos/', views.lista_duenos, name='lista_duenos'),
    path('duenos/crear/', views.crear_dueno, name='crear_dueno'),
    path('duenos/editar/<int:id>/', views.editar_dueno, name='editar_dueno'),
    path('duenos/eliminar/<int:id>/', views.eliminar_dueno, name='eliminar_dueno'),
]