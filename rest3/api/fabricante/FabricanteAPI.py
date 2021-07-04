from api.fabricante.FabricanteSLR import FabricanteSerializado
from api.models import Fabricante
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class FabricanteAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        fabricantes = Fabricante.objects.all()
        serializado = FabricanteSerializado(fabricantes, many=True)

        return Response(serializado.data, status=200)

    def post(self, request):
        data = request.data
        serializado = FabricanteSerializado(data=data)

        if serializado.is_valid():
            serializado.save()
            return Response(serializado.data, status=200)
        else:
            return Response(serializado.errors, status=400)

    def put(self, request, id):
        data = request.data
        fabricante = Fabricante.objects.get(id = id)

        serializado = FabricanteSerializado(fabricante, data=data)

        if serializado.is_valid():
            serializado.save()
            return Response(serializado.data, status=200)
        else:
            return Response(serializado.errors, status=400)

    def delete(self, request, id):
        fabricante = Fabricante.objects.get(id = id)
        fabricante.delete()

        return Response(status=200)