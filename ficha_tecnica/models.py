from distutils.command.upload import upload
from secrets import choice
from django.db import models
from django_currentuser.db.models import CurrentUserField
OPCOES = (
    ('G','GRAMAS'),
    ('L','LITROS'),
)
# Create your models here.


class Prato(models.Model):
    usuario = CurrentUserField()
    nome_do_prato = models.CharField(max_length=120)
    tamanho_receita = models.DecimalField(max_digits=5,decimal_places=1)
    classificacao_tamanho = models.CharField(max_length=1,choices=OPCOES)
    preco_de_venda =  models.DecimalField(max_digits=5,decimal_places=2)
    ##modificar atributo lucro para eliminar erro
    ##CUSTO TOTAL,LUCRO E CMV
class Ingredientes(models.Model):
    prato = models.ForeignKey(Prato,on_delete=models.CASCADE)
    nome_ingrediente = models.CharField(max_length=125)
    classificar_tamanho = models.CharField(max_length=1,choices=OPCOES)
    quantidade_bruta = models.DecimalField(max_digits=5,decimal_places=1)
    quantidade_liquida = models.DecimalField(max_digits=5,decimal_places=1)
    preco_unitario =  models.DecimalField(max_digits=5,decimal_places=2)
   