# Generated by Django 3.1.6 on 2021-02-21 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_auto_20210206_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorias',
            name='descripcion',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Descripcion'),
        ),
    ]
