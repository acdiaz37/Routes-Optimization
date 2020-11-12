# Generated by Django 3.1.3 on 2020-11-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv', models.FileField(blank=True, null=True, upload_to='archivos/', verbose_name='Archivo CSV')),
                ('xlx', models.FileField(blank=True, null=True, upload_to='archivos/', verbose_name='Archivo XLX')),
            ],
        ),
    ]
