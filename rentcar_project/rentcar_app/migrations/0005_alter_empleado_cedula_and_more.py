# Generated by Django 5.1.6 on 2025-02-20 01:05

import rentcar_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentcar_app', '0004_alter_vehiculo_descripcion_alter_vehiculo_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='cedula',
            field=models.CharField(max_length=20, unique=True, validators=[rentcar_app.models.validar_cedula], verbose_name='Cédula'),
        ),
        migrations.AddConstraint(
            model_name='cliente',
            constraint=models.CheckConstraint(condition=models.Q(('limite_credito__gte', 0)), name='limite_credito_no_negativo'),
        ),
    ]
