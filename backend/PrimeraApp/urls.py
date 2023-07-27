from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name = "saludar"),
    path("contact/", views.Contactame, name="contactame"),
    path("RedSocial/", views.RedesSociales, name="Red"),
]
