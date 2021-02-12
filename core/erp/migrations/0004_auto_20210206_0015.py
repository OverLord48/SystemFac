# Generated by Django 3.1.6 on 2021-02-06 00:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_auto_20210202_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=90, verbose_name='Apellido')),
                ('dni', models.CharField(max_length=10, unique=True, verbose_name='Dni')),
                ('fecha_nac', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de nacimiento')),
                ('direccion', models.TextField(max_length=250, verbose_name='Direccion')),
                ('sexo', models.CharField(default='Sexo', max_length=10)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Detalles_venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagen/%Y/%m/%d')),
                ('pvp', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.categorias')),
            ],
            options={
                'verbose_name': 'Nombre',
                'verbose_name_plural': 'Nombres',
            },
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_venta', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de venta')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=2)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.clientes')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.RemoveField(
            model_name='employers',
            name='categ',
        ),
        migrations.RemoveField(
            model_name='employers',
            name='type_id',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Employers',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.AddField(
            model_name='detalles_venta',
            name='venta_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.ventas'),
        ),
    ]
