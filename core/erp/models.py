from django.db import models
from datetime import datetime
# Create your models here.

# class Type(models.Model):
#     name = models.CharField(max_length=150, verbose_name='Nombre')

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'Tipo'
#         verbose_name_plural = 'Tipos'
#         ordering = ['id']

# class Category(models.Model):
#     name = models.CharField(max_length=15, verbose_name='Nombre')

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'Categoria'
#         verbose_name_plural = 'Categorias'
#         ordering = ['id']

# class Employers(models.Model):
#     categ = models.ManyToManyField(Category)
#     type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
#     name = models.CharField(max_length=150, verbose_name='Nombre')
#     dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
#     date_creation = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
#     date_updated = models.DateTimeField(auto_now_add=True)
#     age = models.PositiveIntegerField(default=0)
#     salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     state = models.BooleanField(default=True)
#     avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
#     cvitae = models.FileField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name = 'Empleado'
#         verbose_name_plural = 'Empleados'
#         ordering = ['id']

class Clientes (models.Model):
    nombre = models.CharField(max_length=90, verbose_name='Nombre')
    apellido = models.CharField(max_length=90, verbose_name='Apellido')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    fecha_nac = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    direccion = models.TextField(max_length=250, verbose_name='Direccion')
    sexo = models.CharField(max_length=10, default='Sexo')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Ventas (models.Model):
    fecha_venta = models.DateField(default=datetime.now, verbose_name='Fecha de venta')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=2, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cliente_id = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

class Categorias (models.Model):
    nombre = models.CharField(max_length=90, verbose_name='Nombre', unique=True)
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Productos (models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='imagen/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    categoria_id = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'Nombre'
        verbose_name_plural = 'Nombres'

class Detalles_venta (models.Model):
    cantidad = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    venta_id = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Categorias, on_delete=models.CASCADE)