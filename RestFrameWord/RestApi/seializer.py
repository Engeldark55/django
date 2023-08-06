#lib instalada 
from rest_framework import serializers
#models
from .models import Programador

#clases serializer
class Programador_Serializer(serializers.ModelSerializer):
    class Meta:
        #modelo  para insetractual con el.
        model = Programador
        #campos que quiero interactuar
        #fields = ("FullName","NickName")
        # o para indicar que todos es :
        fields = '__all__'
        # de aqui pase al archivo views