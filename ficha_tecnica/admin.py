from django.contrib import admin

from ficha_tecnica.models import Ingredientes,Prato

# Register your models here.
admin.site.register(Prato)
admin.site.register(Ingredientes)