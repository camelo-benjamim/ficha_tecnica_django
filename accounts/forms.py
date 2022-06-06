from django.contrib.auth import forms
from accounts.models import Account
from django.forms import ModelForm

from django.contrib.auth import admin as adm

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Account
        fields = ("email","proprietario","nome_empresa","segmento_empresa","cnpj","celular","logo","password1","password2")
        labels = { 'email':('Email: '),'nome_empresa': ('Nome da sua empresa (seu negócio): '),'segmento_empresa': ('Segmento da empresa (que sua empresa atua): '),'cnpj':('CNPJ: '), 'celular': ('Número de telefone (incluindo DDD): '),'proprietario': ('Nome do proprietário: '),"logo":('Logo: '),}
        help_texts = {'segmento_empresa':('Por favor escolha o segmento do seu negócio abaixo: '),'celular': ('Por favor, incluir o ddd. Ex: 87999999999'),}
    
class UserChangeForm(forms.UserChangeForm):
    password = forms.ReadOnlyPasswordHashField()
    class Meta(forms.UserChangeForm.Meta):
        model = Account
        fields = ("email","proprietario","nome_empresa","segmento_empresa","cnpj","celular","logo")
        labels = { 'email':('Email: '),'nome_empresa': ('Nome da sua empresa (seu negócio): '),'segmento_empresa': ('Segmento da empresa (que sua empresa atua): '),'cnpj':('CNPJ: '), 'celular': ('Número de telefone (incluindo DDD): '),'proprietário': ('Nome do proprietário: '),'logo':('Logo: '),}
        def clean_password(self):
            return self.initial["password"]

class UserDeleteForm(ModelForm):
    class Meta:
        model = Account
        fields = ['celular']