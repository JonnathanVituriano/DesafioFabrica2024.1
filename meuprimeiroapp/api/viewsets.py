from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from ..models import ViaCepModel
from .serializers import CepSerializer
import requests

class ViaCepViewSet(ModelViewSet):

    queryset = ViaCepModel.objects.all()
    serializer_class = CepSerializer

    def create(self, request):
        cep = request.data.get('cep', '00000000')

        site = "https://viacep.com.br/ws/{cep}/json/"
        
        requisicao = request.get(site)

        json = requisicao.json()

        cep = json.get('cep', '')
        logradouro = json.get('logradouro', '')
        bairro = json.get('bairro', '')
        complemento = json.get('complemento', '')
        localidade = json.get('localidade', '')
        uf = json.get('uf', '')

        dados_recebidos = {
            "cep": f'{cep}',
            "logradouro": f'{logradouro}',
            'bairro': f'{bairro}',
            'complemento': f'{complemento}',
            'localidade': f'{localidade}',
            'uf': f'{uf}'
        }

        meuserializer = CepSerializer(data= dados_recebidos)

        if meuserializer.is_valid():

            cep_pesquisado = ViaCepModel.objects.filter(cep = cep)

            cep_pesquisado_existe = cep_pesquisado.exists()

            if cep_pesquisado_existe:
                return Response({'aviso':f'Ocorreu algum erro te vira'})


            meuserializer.save()
            return meuserializer
        else:
            return Response('deu erro')
