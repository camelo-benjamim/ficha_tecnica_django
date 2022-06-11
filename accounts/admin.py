from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from accounts.models import Account
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    ##Classe model-admin adicionada para funcionametno correto
    ##CustomUserAdmin não foi aplicada devido a menor facilidade de manipulação para caso de alterações internas de credênciais...
    model = Account
    list_display = ['email','nome_empresa',]
    search_fields = ('email','nome_empresa',)
    ordering = ('date_joined',)
    ##para alteração interna dos dados do usuário:
    readonly_fields = ['password','is_staff', 'is_superuser','date_joined','last_login','groups','user_permissions',]
    def has_add_permission(self, request,obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request,obj=None):
        return False

##admin.site.register(Group)
admin.site.register(Account,CustomUserAdmin)
admin.site.unregister(Group)
admin.site.site_header = "My admin "
admin.site.index_title = "Área de administração de dados"

