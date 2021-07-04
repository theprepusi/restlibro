from api.models import Componente
from rest_framework import serializers

class ComponenteSerializado(serializers.ModelSerializer):
    id = serializers.IntegerField(required = False)
    nombre = serializers.CharField(required = False)

    class Meta:
        model = Componente
        fields = '__all__' #['id', 'nombre']