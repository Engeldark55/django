from  django.urls import path, include
from rest_framework import routers
from RestApi import views

router = routers.DefaultRouter()
router.register(r'programadores', views.Programadores_ViewSet)

urlpatterns = [
    path('', include(router.urls))
]