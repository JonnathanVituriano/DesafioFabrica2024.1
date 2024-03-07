from django.db import models

# Create your models here.

class PessoaBancoDados(models.Model):

    primeiro_nome = models.CharField(verbose_name = "Meu primeiro nome", max_length = 20)
    segundo_nome = models.CharField(verbose_name = "Meu segundo nome", max_length = 25)
    idade = models.IntegerField(verbose_name = "Minha Idade", blank = True, null=True)
    
    """
    campo_null = None
    campo_blank = ""
    """

    def __str__(self) -> str:
        return f"{self.primeiro_nome} {self.segundo_nome}"
    
