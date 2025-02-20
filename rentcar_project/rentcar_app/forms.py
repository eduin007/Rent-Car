from django import forms
from .models import Vehiculo, Cliente, Empleado, Inspeccion, Renta

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class InspeccionForm(forms.ModelForm):
    class Meta:
        model = Inspeccion
        fields = '__all__'
        widgets = {
            'estado_gomas': forms.TextInput(attrs={'class': 'form-control'}),  # Caja de texto simple
        }
class RentaForm(forms.ModelForm):
    class Meta:
        model = Renta
        fields = '__all__'