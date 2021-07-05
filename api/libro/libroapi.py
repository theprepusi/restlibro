from api.libro.libroslr import LibroSerial
from api.models import Libro
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class libroapi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            data = request.data
            libros = Libro.objects.all()
            serializado = LibroSerial(libros, many=True)
            libroid = Libro.id()

            return Response(serializado.data, status=200)
        except:
            return Response(status=400)

    def post(self, request):
        data = request.data
        serializado = LibroSerial(data=data)

        if serializado.is_valid():
            serializado.save()
            return Response(serializado.data, status=200)
        else:
            return Response(serializado.errors, status=400)

    def put(self, request, id):
        data = request.data
        libro = Libro.objects.get(id = id)

        serializado = LibroSerial(libro, data=data)

        if serializado.is_valid():
            serializado.save()
            return Response(serializado.data, status=200)
        else:
            return Response(serializado.errors, status=400)

    def delete(self, request, id):
        libro = Libro.objects.get(id = id)
        libro.delete()
        return Response(status=200)