from django.contrib import admin
from tienda.models import Categoria, Cartera, Pedido


# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)

@admin.register(Cartera)
class CarteraAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "categoria", "descripcion", "precio", "stock", "activo")  
    list_filter = ("categoria", "activo")
    search_fields = ("nombre", "descripcion", "categoria__nombre")
    ordering = ("nombre",)
    list_editable = ("descripcion", "precio", "stock", "activo")
    fields = ("nombre", "categoria", "descripcion", "precio", "stock", "activo")
    
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "cartera", "cantidad", "fecha")
    list_filter = ("cartera", "fecha")
    search_fields = ("cartera__nombre",)
    date_hierarchy = "fecha"
    ordering = ("-fecha",)