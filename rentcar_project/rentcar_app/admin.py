from django.contrib import admin
from .models import (
    TipoVehiculo, Marca, Modelo, TipoCombustible,
    Vehiculo, Cliente, Empleado, Inspeccion, Renta
)

# Registrar todos los modelos en el panel de administración
admin.site.register(TipoVehiculo)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(TipoCombustible)
admin.site.register(Vehiculo)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Inspeccion)
admin.site.register(Renta)