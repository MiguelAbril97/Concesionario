from django.contrib import admin
from .models  import Vendedor, Coche, Venta
# Register your models here.
admin.site.register(Vendedor)
admin.site.register(Coche)
admin.site.register(Venta)