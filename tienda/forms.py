from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Categoria, Cartera, Pedido

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre", "descripcion"]

class CarteraForm(forms.ModelForm):
    class Meta:
        model = Cartera
        fields = ["nombre", "categoria", "descripcion", "precio", "stock", "activo"]
       
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["cartera", "cantidad"]

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")