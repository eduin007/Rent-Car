from django.urls import path
from . import views
from .views import generar_reporte_pdf


urlpatterns = [
    path('reporte/pdf/', generar_reporte_pdf, name='reporte_rentas_pdf'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('empleado_home/', views.empleado_home, name='empleado_home'),
    path('', views.home, name='home'),
    path('vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
    path('vehiculos/crear/', views.crear_vehiculo, name='crear_vehiculo'),
    path('vehiculos/editar/<int:id>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('vehiculos/eliminar/<int:id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/crear/', views.crear_empleado, name='crear_empleado'),
    path('inspecciones/', views.lista_inspecciones, name='lista_inspecciones'),
    path('inspecciones/crear/', views.crear_inspeccion, name='crear_inspeccion'),
    path('rentas/', views.lista_rentas, name='lista_rentas'),
    path('rentas/crear/', views.crear_renta, name='crear_renta'),
    path('consultas/rentas_por_cliente/', views.consulta_rentas_por_cliente, name='consulta_rentas_por_cliente'),
    path('reportes/rentas_entre_fechas/', views.reporte_rentas_entre_fechas, name='reporte_rentas_entre_fechas'),
    path('vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('rentas/', views.lista_rentas, name='lista_rentas'),
    path('inspecciones/', views.lista_inspecciones, name='lista_inspecciones'),
    path('marcas/', views.lista_marcas, name='lista_marcas'),
    path('modelos/', views.lista_modelos, name='lista_modelos'),
    path('alquileres/', views.lista_alquileres, name='lista_alquileres'),
    path('tipos-combustible/', views.lista_tipos_combustible, name='lista_tipos_combustible'),
    path('tipos-vehiculos/', views.lista_tipos_vehiculos, name='lista_tipos_vehiculos'),
    path('reportes/', views.reportes, name='reportes'),
]