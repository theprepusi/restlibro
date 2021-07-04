from api.producto.ProductoSRL import ProductoSerializado
from api.usuario.UsuarioSRL import UsuarioSerializado
from api.models import Cuenta
from rest_framework import serializers

class CuentaSerializada(serializers.ModelSerializer):
    usuario = UsuarioSerializado(required = False)
    productos = ProductoSerializado(required = False, many=True)

    class Meta:
        model = Cuenta
        fields = ['usuario', 'productos']