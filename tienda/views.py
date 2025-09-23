from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.db.models import Q
from tienda.models import Cartera, Pedido, Categoria
from .forms import CategoriaForm, CarteraForm, PedidoForm, RegistroForm

# Create your views here.

# FUNCIONES ESTATICAS: Se realiza unicamente un render y llamar al html asociado.

# Inicio
def inicio(request):
    return render(request, 'tienda/inicio.html')

# Info Contacto
def contacto_view(request):
    return render(request, 'tienda/contacto.html')

# Politica de Devolucion
def politicas_view(request):
    return render(request, 'tienda/politicas.html')

# Terminos y Condiciones
def terminos_view(request):
    return render(request, 'tienda/terminos.html')



# FUNCIONES DEPENDIENTES A LA BD: Se definen en models

# Carteras
def cartera_list(request):
    qs = Cartera.objects.select_related("categoria").filter(activo=True)

    q = (request.GET.get("q") or "").strip()
    if q:
        qs = qs.filter(
            Q(nombre__icontains=q) |
            Q(descripcion__icontains=q) |
            Q(categoria__nombre__icontains=q)
        )

    cat = (request.GET.get("cat") or "").strip()
    if cat:
        qs = qs.filter(categoria_id=cat)

    return render(request, "tienda/cartera_list.html", {"carteras": qs})


# Pedidos
def pedir_cartera(request, cartera_id):
    # Crea pedido y descuenta stock
    if request.method == 'POST':
        cartera = get_object_or_404(Cartera, id=cartera_id)
        cantidad = int(request.POST.get('cantidad', 1))

        if cartera.stock >= cantidad:
            Pedido.objects.create(cartera=cartera, cantidad=cantidad)
            cartera.stock -= cantidad
            cartera.save()
        
        return redirect('cartera_list')

    return redirect('cartera_list')


# FUNCIONES DE INTERACCIÓN

# Crear categoría
def categoria_nueva(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cartera_list")  # redirige al listado
    else:
        form = CategoriaForm()
    return render(request, "tienda/forms.html", {"form": form, "titulo": "Nueva categoría"})


# Crear cartera
def cartera_nueva(request):
    if request.method == "POST":
        form = CarteraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cartera_list")
    else:
        form = CarteraForm()
    return render(request, "tienda/forms.html", {"form": form, "titulo": "Nueva cartera"})


# Crear pedido
def pedido_nuevo(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cartera_list")
    else:
        form = PedidoForm()
    return render(request, "tienda/forms.html", {"form": form, "titulo": "Nuevo pedido"})


# Registro
def registro_view(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()  
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user_auth = authenticate(request, username=username, password=raw_password)
            if user_auth is not None:
                auth_login(request, user_auth)
            return redirect("inicio")
    else:
        form = RegistroForm()
    return render(request, "tienda/registro.html", {"form": form})


# Login simple
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("inicio")
        return render(request, "tienda/login.html", {"error": "Usuario o contraseña inválidos."})
    return render(request, "tienda/login.html")


# Logout
def logout_view(request):
    auth_logout(request)
    return redirect("inicio")