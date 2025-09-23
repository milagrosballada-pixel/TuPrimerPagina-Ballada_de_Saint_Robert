from django.urls import path
from tienda import views

urlpatterns = [
    # Home
    path('', views.inicio, name='inicio'),
    # Productos
    path('carteras/', views.cartera_list, name='cartera_list'),
    path("carteras/pedir/<int:cartera_id>/", views.pedir_cartera, name="pedir_cartera"),
    # Info
    path('contacto/', views.contacto_view, name='contacto'),
    path('politicas/', views.politicas_view, name='politicas'),
    path('terminos/', views.terminos_view, name='terminos'),
    # Registro
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("registro/", views.registro_view, name="registro"),
    # Forms
    path("categorias/nueva/", views.categoria_nueva, name="categoria_nueva"),
    path("carteras/nueva/", views.cartera_nueva, name="cartera_nueva"),
    path("pedidos/nuevo/", views.pedido_nuevo, name="pedido_nuevo"),
]