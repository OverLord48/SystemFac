# Generated by Django 3.1.6 on 2021-02-02 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_auto_20210202_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='employers',
            name='categ',
            field=models.ManyToManyField(to='erp.Category'),
        ),
    ]
