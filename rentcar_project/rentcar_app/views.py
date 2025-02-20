from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo, Cliente, Empleado, Inspeccion, Renta
from .forms import VehiculoForm, ClienteForm, EmpleadoForm, InspeccionForm, RentaForm
from .models import Marca, Modelo, Alquiler, TipoCombustible, TipoVehiculo
from .models import Renta
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
 
def generar_reporte_pdf(request):
    # Crear la respuesta HTTP con contenido tipo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_rentas.pdf"'

    # Crear el objeto PDF
    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.setTitle("Reporte de Rentas")

    # Configurar fuente y título
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, 750, "Reporte de Rentas")

    # Dibujar líneas de datos
    pdf.setFont("Helvetica", 12)
    y = 720  # Posición inicial en Y

    rentas = Renta.objects.all()  # Obtener todas las rentas

    for renta in rentas:
        pdf.drawString(100, y, f"Vehículo: {renta.vehiculo.descripcion} | Cliente: {renta.cliente.nombre} | Desde: {renta.fecha_renta} | Hasta: {renta.fecha_devolucion}")
        y -= 20  # Mover hacia abajo para la próxima línea

        # Si llegamos al final de la página, agregamos una nueva
        if y < 50:
            pdf.showPage()
            pdf.setFont("Helvetica", 12)
            y = 750

    # Guardar y cerrar el PDF
    pdf.showPage()
    pdf.save()

    return response

def reportes(request):
    # Lógica para generar reportes (puedes personalizarla según tus necesidades)
    rentas = Renta.objects.all()  # Ejemplo: Obtener todas las rentas
    return render(request, 'rentcar_app/reportes/reportes.html', {'rentas': rentas})
def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'rentcar_app/marcas/lista.html', {'marcas': marcas})

def lista_modelos(request):
    modelos = Modelo.objects.all()
    return render(request, 'rentcar_app/modelos/lista.html', {'modelos': modelos})

def lista_alquileres(request):
    alquileres = Alquiler.objects.all()
    return render(request, 'rentcar_app/alquileres/lista.html', {'alquileres': alquileres})

def lista_tipos_combustible(request):
    tipos_combustible = TipoCombustible.objects.all()
    return render(request, 'rentcar_app/tipos_combustible/lista.html', {'tipos_combustible': tipos_combustible})

def lista_tipos_vehiculos(request):
    tipos_vehiculos = TipoVehiculo.objects.all()
    return render(request, 'rentcar_app/tipos_vehiculos/lista.html', {'tipos_vehiculos': tipos_vehiculos})
# Vista para la página de inicio
def home(request):
    return render(request, 'rentcar_app/home.html')

# Vistas para Vehículos
def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'rentcar_app/vehiculos/lista.html', {'vehiculos': vehiculos})

def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'rentcar_app/vehiculos/crear.html', {'form': form})

def editar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'rentcar_app/vehiculos/editar.html', {'form': form})

def eliminar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('lista_vehiculos')
    return render(request, 'rentcar_app/vehiculos/eliminar.html', {'vehiculo': vehiculo})

# Vistas para Clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'rentcar_app/clientes/lista.html', {'clientes': clientes})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'rentcar_app/clientes/crear.html', {'form': form})

# Vistas para Empleados
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'rentcar_app/empleados/lista.html', {'empleados': empleados})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'rentcar_app/empleados/crear.html', {'form': form})

# Vistas para Inspecciones
def lista_inspecciones(request):
    inspecciones = Inspeccion.objects.all()
    return render(request, 'rentcar_app/inspecciones/lista.html', {'inspecciones': inspecciones})

def crear_inspeccion(request):
    if request.method == 'POST':
        form = InspeccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_inspecciones')
    else:
        form = InspeccionForm()
    return render(request, 'rentcar_app/inspecciones/crear.html', {'form': form})

# Vistas para Rentas
def lista_rentas(request):
    rentas = Renta.objects.all()
    return render(request, 'rentcar_app/rentas/lista.html', {'rentas': rentas})

def crear_renta(request):
    if request.method == 'POST':
        form = RentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_rentas')
    else:
        form = RentaForm()
    return render(request, 'rentcar_app/rentas/crear.html', {'form': form})

# Consultas y Reportes
def consulta_rentas_por_cliente(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente_id')
        rentas = Renta.objects.filter(cliente_id=cliente_id)
        return render(request, 'rentcar_app/consultas/rentas_por_cliente.html', {'rentas': rentas})
    return render(request, 'rentcar_app/consultas/rentas_por_cliente.html')

def reporte_rentas_entre_fechas(request):
    if request.method == 'POST':
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        rentas = Renta.objects.filter(fecha_renta__range=[fecha_inicio, fecha_fin])
        return render(request, 'rentcar_app/reportes/rentas_entre_fechas.html', {'rentas': rentas})
    return render(request, 'rentcar_app/reportes/rentas_entre_fechas.html')

# rentcar_app/views.py
from django.shortcuts import render, redirect

def home(request):
    if request.method == 'POST':
        # Lógica para manejar el login
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Aquí puedes agregar la lógica para verificar si es empleado o administrador
        if username == 'admin' and password == 'admin123':
            return redirect('admin_home')  # Redirige al administrador
        elif username == 'empleado' and password == 'empleado123':
            return redirect('empleado_home')  # Redirige al empleado
        else:
            # Si las credenciales son incorrectas, muestra un mensaje de error
            return render(request, 'rentcar_app/login.html', {'error': 'Credenciales incorrectas'})
    
    # Si es una solicitud GET, muestra el formulario de login
    return render(request, 'rentcar_app/login.html')

def admin_home(request):
    return render(request, 'rentcar_app/admin_home.html')

def empleado_home(request):
    return render(request, 'rentcar_app/empleado_home.html')
# Vistas para Clientes
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'rentcar_app/clientes/lista.html', {'clientes': clientes})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'rentcar_app/clientes/crear.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'rentcar_app/clientes/editar.html', {'form': form})

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'rentcar_app/clientes/eliminar.html', {'cliente': cliente})