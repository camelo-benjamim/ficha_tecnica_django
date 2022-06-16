from typing import Text
from django import forms
from django.shortcuts import get_object_or_404
from ficha_tecnica.models import *
from accounts.models import Account

class FormPrato(forms.ModelForm):         
    class Meta:
        model = Prato
        fields = ['nome_do_prato','tamanho_receita','classificacao_tamanho','preco_de_venda']
        labels = {'nome_do_prato':('Nome do prato: '),'tamanho_receita':('Tamanho da receita: '),'classificacao_tamanho':('Classificação tamanho: '),'preco_de_venda':('Preço de venda: ')}
        
### ITENS
class FormIngredientes(forms.ModelForm):
    def __init__(self, id_usr,*args, **kwargs): 
            super(FormIngredientes, self).__init__(*args, **kwargs)
            ##pegando obj
            usuario = get_object_or_404(Account,id=id_usr)
            pratos = Prato.objects.filter(usuario=usuario)
            self.fields['prato'].queryset = pratos
    class Meta:
        model = Ingredientes
        fields = ['nome_ingrediente','prato','classificar_tamanho','quantidade_bruta','quantidade_liquida','preco_unitario']
        labels = {'nome_ingrediente':('Nome do ingrediente: '), 'classificar_tamanho':('Classificar tamanho: '),'quantidade_bruta':('Quantidade bruta:'),'quantidade_liquida':('Quantidade líquida:'),'preco_unitario':('Preço unitário: ')}
    

