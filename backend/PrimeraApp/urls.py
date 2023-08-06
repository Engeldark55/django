from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name = "index"),
    path("contact/", views.Contactame, name="contactame"),
    path("RedSocial/", views.RedesSociales, name="Red_Social"),
    path("crear_articulo/", views.CrearArticulo, name="crear_articulo"),
    path("FormArt/", views.FormArticulo, name="FormArt"),
    path("VistaArticulos/",views.ObtenerArticulo, name="verArticulo"),
    path("actualizarArticulo/<int:id>", views.actualizarArticulo, name="actualizarArt")
]
