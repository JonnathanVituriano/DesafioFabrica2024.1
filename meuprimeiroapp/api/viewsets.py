from rest_framework.viewsets import ModelViewSet
from .serializers import PessoaSerializer
from ..models import PessoaBancoDados

class PessoaViewSet(ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = PessoaBancoDados.objects.all()

