from rest_framework.serializers import ModelSerializer
from ..models import PessoaBancoDados

class PessoaSerializer(ModelSerializer):
    class Meta:
        model = PessoaBancoDados
        fields = ['id', 'primeiro_nome', 'segundo_nome', 'idade']
