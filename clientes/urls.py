from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_orden, name='registrar_orden'),
    path('orden-exitosa/<int:idOrden>/', views.orden_exitosa, name='orden_exitosa'),
    path('mis-ordenes/', views.mis_ordenes, name='mis_ordenes'),
]