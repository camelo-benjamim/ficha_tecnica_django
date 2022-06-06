from django.contrib import admin
from accounts.models import Account, SegmentoEmpresa
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    ##Classe model-admin adicionada para funcionametno correto
    ##CustomUserAdmin não foi aplicada devido a menor facilidade de manipulação para caso de alterações internas de credênciais...
    model = Account
    list_display = ['proprietario','email','nome_empresa','celular','cnpj']
    search_fields = ('email','proprietario','nome_empresa','celular',)
    ordering = ('date_joined',)
    ##para alteração interna dos dados do usuário:
    readonly_fields = ['password','is_staff', 'is_superuser','date_joined','last_login','groups','user_permissions',]
    def has_add_permission(self, request,obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request,obj=None):
        return False
class CustomSegmento(admin.ModelAdmin):
    model = SegmentoEmpresa
    list_display = ['nome_segmento',]
    ordering = ('-id',)

    def has_add_permission(self,request,obj=None):
        return True
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self,request,obj=None):
        return True 

##admin.site.register(Group)
admin.site.register(Account,CustomUserAdmin)
admin.site.register(SegmentoEmpresa,CustomSegmento)
admin.site.unregister(Group)
admin.site.site_header = "My admin "
admin.site.index_title = "Área de administração de dados"

