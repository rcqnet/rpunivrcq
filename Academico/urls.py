from django.urls import path
from . import views
from rest_framework import routers
from .api import AcademicoViewSet

router = routers.DefaultRouter()

router.register('api/Academico', AcademicoViewSet, 'Academico')

urlpatterns = router.urls

urlpatterns = [
    path('', views.home),
    path('registroCurso/', views.registrar_curso),
    path('edicionCurso/<id>', views.edicionCurso),    
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<id>', views.eliminar_curso)
]
