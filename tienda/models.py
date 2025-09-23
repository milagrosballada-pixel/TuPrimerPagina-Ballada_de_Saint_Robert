from django.db import models
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
    

class Cartera(models.Model):
    nombre = models.CharField(max_length=120)
    categoria = models.ForeignKey(            # Relacion muchos a uno
        Categoria,                          
        on_delete=models.SET_NULL,            # Si se borra la categoria 
        null=True,                            # Se permite que quede vacio
        related_name='carteras'
    )    
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        if self.categoria:
            return f"{self.nombre} ({self.categoria.nombre})"
        return self.nombre


class Pedido(models.Model):
    cartera = models.ForeignKey(        # Relacion muchos a uno
        Cartera,                        
        on_delete=models.CASCADE,       # Si se borra la cartera, se borran los pedidos relacionados
        related_name='pedidos')
    cantidad = models.PositiveIntegerField(default=1)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido #{self.id} - {self.cartera.nombre} x {self.cantidad}'
    