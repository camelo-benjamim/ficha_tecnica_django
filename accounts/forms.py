from django.contrib.auth import forms
from accounts.models import Account
from django.forms import ModelForm

from django.contrib.auth import admin as adm

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Account
        fields = ("email","nome_empresa","password1","password2")
        labels = { 'email':('Email: '),'nome_empresa': ('Nome da sua empresa (seu negócio): '),}
    
class UserChangeForm(forms.UserChangeForm):
    password = forms.ReadOnlyPasswordHashField()
    class Meta(forms.UserChangeForm.Meta):
        model = Account
        fields = ("email","nome_empresa",)
        labels = { 'email':('Email: '),'nome_empresa': ('Nome da sua empresa (seu negócio): '),}
        def clean_password(self):
            return self.initial["password"]

class UserDeleteForm(ModelForm):
    class Meta:
        model = Account
        fields = ['email']