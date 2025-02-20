from django.db import models
from django.core.exceptions import ValidationError
class Alquiler(models.Model):
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.CASCADE)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    fecha_alquiler = models.DateField()
    fecha_devolucion = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Alquiler {self.id} - {self.vehiculo.descripcion}"
# Modelo para Tipos de Vehículos
class TipoVehiculo(models.Model):
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")
    estado = models.BooleanField(default=True, verbose_name="Estado (Activo)")

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Tipo de Vehículo"
        verbose_name_plural = "Tipos de Vehículos"


# Modelo para Marcas
class Marca(models.Model):
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")
    estado = models.BooleanField(default=True, verbose_name="Estado (Activo)")

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"


# Modelo para Modelos
class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Marca")
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")
    estado = models.BooleanField(default=True, verbose_name="Estado (Activo)")

    def __str__(self):
        return f"{self.marca.descripcion} - {self.descripcion}"

    class Meta:
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"


# Modelo para Tipos de Combustible
class TipoCombustible(models.Model):
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")
    estado = models.BooleanField(default=True, verbose_name="Estado (Activo)")

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = "Tipo de Combustible"
        verbose_name_plural = "Tipos de Combustible"


# Modelo para Vehículos
class Vehiculo(models.Model):
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")
    no_chasis = models.CharField(max_length=50, verbose_name="Número de Chasis", unique=True)
    no_motor = models.CharField(max_length=50, verbose_name="Número de Motor", unique=True)
    no_placa = models.CharField(max_length=20, verbose_name="Número de Placa", unique=True)
    tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE, verbose_name="Tipo de Vehículo")
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Marca")
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, verbose_name="Modelo")
    tipo_combustible = models.ForeignKey(TipoCombustible, on_delete=models.CASCADE, verbose_name="Tipo de Combustible")
    estado = models.BooleanField(default=True, verbose_name="Estado (Activo)")

    def __str__(self):
        return f"{self.descripcion} - {self.no_placa}"

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"


# Modelo para Clientes


def validar_cedula(cedula):
    """ Valida si una cédula dominicana es correcta """
    cedula = cedula.replace("-", "").strip()
    
    # Verificar que tenga 11 dígitos numéricos
    if not cedula.isdigit() or len(cedula) != 11:
        raise ValidationError("La cédula ingresada no es válida.")
    
    # Algoritmo de validación de cédula dominicana
    suma = 0
    pesos = [1, 2] * 5  # Secuencia de multiplicadores (1,2 repetidos)
    
    for i in range(10):  # Solo iteramos los primeros 10 dígitos
        resultado = int(cedula[i]) * pesos[i]
        if resultado >= 10:
            resultado = (resultado // 10) + (resultado % 10)
        suma += resultado
    
    digito_verificador = (10 - (suma % 10)) % 10
    
    if digito_verificador != int(cedula[-1]):  # Comparar con el último dígito
        raise ValidationError("La cédula ingresada no es válida.")

# Modelo para Clientes
class Cliente(models.Model):
    TIPO_PERSONA_CHOICES = [
        ('F', 'Física'),
        ('J', 'Jurídica'),
    ]

    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    cedula = models.CharField(max_length=20, verbose_name="Cédula", unique=True)
    no_tarjeta_cr = models.CharField(max_length=20, verbose_name="Número de Tarjeta de Crédito")
    limite_credito = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Límite de Crédito")
    tipo_persona = models.CharField(max_length=1, choices=TIPO_PERSONA_CHOICES, verbose_name="Tipo de Persona")
    estado = models.BooleanField(default=True, verbose_name="Estado (Activo)")

    def __str__(self):
        return f"{self.nombre} - {self.cedula}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        constraints = [
            models.CheckConstraint(
                check=models.Q(limite_credito__gte=0),  # No permite valores negativos
                name="limite_credito_no_negativo"
            ),
        ]
# Modelo para Empleados
class Empleado(models.Model):
    TANDA_LABOR_CHOICES = [
        ('M', 'Matutina'),
        ('V', 'Vespertina'),
        ('N', 'Nocturna'),
    ]

    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    cedula = models.CharField(max_length=20, verbose_name="Cédula", unique=True, validators=[validar_cedula])
    tanda_labor = models.CharField(max_length=1, choices=TANDA_LABOR_CHOICES, verbose_name="Tanda Laboral")
    porciento_comision = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Porcentaje de Comisión")
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso")
    estado = models.BooleanField(default=True, verbose_name="Estado (Activo)")

    def __str__(self):
        return f"{self.nombre} - {self.cedula}"

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"


# Modelo para Inspección
class Inspeccion(models.Model):
    COMBUSTIBLE_CHOICES = [
        ('1/4', '1/4 de Tanque'),
        ('1/2', '1/2 de Tanque'),
        ('3/4', '3/4 de Tanque'),
        ('Lleno', 'Tanque Lleno'),
    ]

    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, verbose_name="Vehículo")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    tiene_ralladuras = models.BooleanField(default=False, verbose_name="Tiene Ralladuras")
    cantidad_combustible = models.CharField(max_length=10, choices=COMBUSTIBLE_CHOICES, verbose_name="Cantidad de Combustible")
    tiene_goma_repuesta = models.BooleanField(default=False, verbose_name="Tiene Goma de Repuesto")
    tiene_gato = models.BooleanField(default=False, verbose_name="Tiene Gato")
    tiene_roturas_cristal = models.BooleanField(default=False, verbose_name="Tiene Roturas de Cristal")
    estado_gomas = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField(verbose_name="Fecha de Inspección")
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Empleado que Realiza la Inspección")
    estado = models.BooleanField(default=True, verbose_name="Estado (Activo)")

    def __str__(self):
        return f"Inspección #{self.id} - {self.vehiculo.no_placa}"

    class Meta:
        verbose_name = "Inspección"
        verbose_name_plural = "Inspecciones"


# Modelo para Renta y Devolución
class Renta(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Empleado")
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, verbose_name="Vehículo")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    fecha_renta = models.DateField(verbose_name="Fecha de Renta")
    fecha_devolucion = models.DateField(verbose_name="Fecha de Devolución")
    monto_dia = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto por Día")
    cantidad_dias = models.IntegerField(verbose_name="Cantidad de Días")
    comentario = models.TextField(verbose_name="Comentario", blank=True, null=True)
    estado = models.BooleanField(default=True, verbose_name="Estado (Activo)")

    def __str__(self):
        return f"Renta #{self.id} - {self.cliente.nombre}"

    class Meta:
        verbose_name = "Renta"
        verbose_name_plural = "Rentas"