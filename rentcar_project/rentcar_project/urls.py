from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Importa HttpResponse
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


urlpatterns = [
    path('home', admin.site.urls),
    path('', home, name='home'),  # Ruta para la página principal
    path('home/', admin.site.urls),
    path('', include('rentcar_app.urls'))
]
