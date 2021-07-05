from api.models import Libro
from rest_framework import serializers

class LibroSerial(serializers.ModelSerializer):
    id = serializers.IntegerField(required = False)
    nombre = serializers.CharField(required = False)

    class Meta:
        model = Libro
        fields = '__all__' #['id', 'nombre']