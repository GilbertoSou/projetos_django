from django.urls import path
from .views import ProjetoListAPIView,  EquipeListAPIView


urlpatterns = [
  path('projetos', ProjetoListAPIView.as_view()),
  path('equipes', EquipeListAPIView.as_view()),
]