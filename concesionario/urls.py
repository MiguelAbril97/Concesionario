from django.urls import path
from . import views

urlpatterns = [
    path('vendedor/', views.verVendedores, name='verVendedores.html'),
    path('coches/', views.verCoches, name='verCoches.html'),
    path('ventas/', views.verVentas, name='verVentas.html'),
]
