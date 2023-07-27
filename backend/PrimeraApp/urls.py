from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name = "index"),
    path("contact/", views.Contactame, name="contactame"),
    path("RedSocial/", views.RedesSociales, name="Red_Social"),
]
