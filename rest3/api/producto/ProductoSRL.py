from api.componente.ComponenteSRL import ComponenteSerializado
from api.fabricante.FabricanteSLR import FabricanteSerializado
from api.models import Producto
from rest_framework import serializers

class ProductoSerializado(serializers.ModelSerializer):
    id = serializers.IntegerField(required = False)
    nombre = serializers.CharField(required = False)
    fabricante = FabricanteSerializado(required = False)
    componente = ComponenteSerializado(required = False)
    precio = serializers.IntegerField(required = False)
    stock = serializers.IntegerField(required = False)

    class Meta:
        model = Producto
        fields = '__all__' #['id', 'nombre']