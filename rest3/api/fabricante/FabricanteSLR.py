from api.models import Fabricante
from rest_framework import serializers

class FabricanteSerializado(serializers.ModelSerializer):
    id = serializers.IntegerField(required = False)
    nombre = serializers.CharField(required = False)

    class Meta:
        model = Fabricante
        fields = '__all__' #['id', 'nombre']