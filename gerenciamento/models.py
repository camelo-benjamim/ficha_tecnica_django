from django.db import models
from accounts.models import Account
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

# As model field:
from django_currentuser.db.models import CurrentUserField
# Create your models here.
class Classificacao(models.Model):
    classificacao = models.CharField(max_length=35)
    proprietario = CurrentUserField()
class Produto(models.Model):
    nome_produto = models.CharField(max_length=120)
    codigo_de_barras = models.CharField(max_length=13,blank=True)
    preco_compra = models.DecimalField(max_digits=7,decimal_places=2)
    preco_venda = models.DecimalField(max_digits=7,decimal_places=2)
    descricao = models.TextField()
    imagem_produto = models.ImageField(upload_to="produtos/")
    ativo = models.BooleanField(default=True)
    classificacao = models.ForeignKey(Classificacao,on_delete=models.PROTECT)
    proprietario_produto = CurrentUserField()