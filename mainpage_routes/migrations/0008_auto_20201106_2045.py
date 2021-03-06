# Generated by Django 3.1.3 on 2020-11-07 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage_routes', '0007_auto_20201106_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='direccion',
            field=models.CharField(choices=[('DEPOSITO_BOG', 'Calle 22 #56-24'), ('DEPOSITO_CTG', 'Carrera 44 #31A-77')], default='DEPOSITO_BOG', help_text='Especifique la dirección donde el vehículo se encuentra ubicado', max_length=15, verbose_name='Dirección de la ubicación del vehículo'),
        ),
    ]
