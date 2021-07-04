from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

# API QUE VERIFICA QUE LOS DATOS DEL USUARIO SEAN CORRECTOS PARA GENERAR UN TOKEN DE AUTENTICACION.
class LoginAPI(APIView):
    def post(self, request):
        data = request.data

        username = data['username']
        password = data['password']

        try:
            user = User.objects.get(username=username)
        except:
            return Response({"Error": "usuario no valido."}, status=400)

        password_valido = check_password(password, user.password)

        if( password_valido ):
            token, created = Token.objects.get_or_create(user=user)

            return Response({"Token": token.key}, status=200)
        else:
            return Response({"Error": "contraseña no valida."}, status=400)


# API QUE ELIMINA EL TOKEN DE LA CUENTA.
class LogoutAPI(APIView):
    def post(self, request):
        try:
            data  = request.data
            token = data['token']
            token = Token.objects.filter(key = token)
            token.delete()
            
            return Response(status=200)
        except:
            return Response(status=400)