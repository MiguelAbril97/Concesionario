from django.shortcuts import render
from .models import Vendedor, Coche, Venta

# Create your views here.
def verVendedores(request):
    vista = Vendedor.objects.all()
    return render(request, 'concesionario/verVendedores.html',{'Vendedor_mostrar' : vista} )

def verCoches(request):
    vista = Coche.objects.all()
    return render(request, 'concesionario/verCoches.html',{'Coche_mostrar' : vista} )

def verVentas(request):
    vista = Venta.objects.all()
    return render(request, 'concesionario/verVentas.html',{'Venta_mostrar' : vista} )