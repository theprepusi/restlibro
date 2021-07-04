from api.usuario.UsuarioSRL import UsuarioSerializado
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

class UsuarioAPI(APIView):
    def get(self, request):
        usuarios = User.objects.all()
        
        serializado = UsuarioSerializado(usuarios, many=True)
        print(serializado.data)

        return Response(serializado.data, status=200)