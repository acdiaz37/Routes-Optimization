# Generated by Django 3.1.3 on 2020-11-07 16:11

from django.db import migrations, models
import login_routes.models


class Migration(migrations.Migration):

    dependencies = [
        ('login_routes', '0002_auto_20201106_0054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Conductor', 'verbose_name_plural': 'Conductores'},
        ),
        migrations.AlterModelManagers(
            name='users',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='users',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='users',
            name='username',
        ),
        migrations.AddField(
            model_name='users',
            name='active',
            field=models.BooleanField(default=True, help_text='Especifique el estado activo de este usuario en el portal', verbose_name='¿Cuenta activa?'),
        ),
        migrations.AddField(
            model_name='users',
            name='admin',
            field=models.BooleanField(default=False, help_text='Indique si este usuario tiene privilegios de superusuario en el portal', verbose_name='¿Administrador del portal?'),
        ),
        migrations.AddField(
            model_name='users',
            name='cedula',
            field=models.CharField(default='2720630968', help_text='Indique su número de cédula o licencia de conducir para su identificación en el sistema', max_length=10, unique=True, validators=[login_routes.models.only_digits], verbose_name='Número de cédula'),
        ),
        migrations.AddField(
            model_name='users',
            name='licencia',
            field=models.CharField(default='186947860801512', help_text='Indique su número de licencia de conducir para su identificación en el sistema', max_length=15, unique=True, validators=[login_routes.models.only_digits], verbose_name='Número de licencia de conducción'),
        ),
        migrations.AddField(
            model_name='users',
            name='staff',
            field=models.BooleanField(default=True, help_text='Clarifique si este usuario hace parte del staff del portal', verbose_name='¿Personal del sitio?'),
        ),
    ]