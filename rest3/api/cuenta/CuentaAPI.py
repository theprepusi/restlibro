from api.cuenta.CuentaSRL import CuentaSerializada
from api.models import Cuenta
from api.usuario.UsuarioSRL import UsuarioSerializado
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

class CuentaAPI(APIView):
    def get(self, request, id):
        usuario = User.objects.get(id=id)
        cuenta = Cuenta.objects.get(usuario=usuario)
        
        serializado = CuentaSerializada(cuenta)

        return Response(serializado.data, status=200)