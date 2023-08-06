from rest_framework import viewsets
from .seializer import Programador_Serializer
from .models import Programador

# Create your views here.
class Programadores_ViewSet(viewsets.ModelViewSet):
    #listar elementos del modelo
    queryset = Programador.objects.all()
    serializer_class = Programador_Serializer



