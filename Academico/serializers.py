from rest_framework import serializers
from .models import Curso

class AcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id', 'nombre', 'credito')
        read_only_fields = ('id', )
        