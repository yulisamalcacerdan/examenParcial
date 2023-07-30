from django.db import models

# Create your models here.
class tienda(models.Model):
    direccion = models.CharField(max_length=50, blank=True, null=True)
    provincia = models.CharField(max_length=30, blank=True, null=True)
    Region = models.CharField(max_length=30, blank=True, null=True)
    fechaCreacion = models.CharField(max_length=30, blank=True, null=True)    
    telefono = models.CharField(max_length=9, blank=True, null=True)    

class producto(models.Model):
    descripcion = models.CharField(max_length=35, blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    precioVenta = models.CharField(max_length=35, blank=True, null=True)
    cantidad = models.CharField(max_length=35, blank=True, null=True)
    tiendaProducto = models.OneToOneField(tienda, on_delete=models.SET_NULL, blank=True, null=True)







