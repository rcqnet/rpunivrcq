from .models import Curso
from rest_framework import viewsets, permissions
from .serializers import AcademicoSerializer

class AcademicoViewSet(viewsets.ModelViewSet):
    Curso.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AcademicoSerializer
    