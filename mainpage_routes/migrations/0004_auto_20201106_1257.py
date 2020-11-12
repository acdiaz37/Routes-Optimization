# Generated by Django 3.1.3 on 2020-11-06 17:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage_routes', '0003_cliente_despacho_pedido_vehiculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='despacho',
            name='fecha_despacho',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, help_text='Fecha autogenerada para el despacho el día que se registre', verbose_name='Fecha de registro del despacho'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='despacho',
            name='vehiculo',
            field=models.ForeignKey(help_text='Indique cual será el vehículo destinado para realizar el despacho asignado', null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainpage_routes.vehiculo', verbose_name='Vehículo asignado'),
        ),
    ]