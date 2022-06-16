from django import urls
from django.db.models.fields import CharField 
from django.urls.conf import path, include
from ficha_tecnica.views import *


urlpatterns = [
    path('', mainView),
    ##prato
    path('visualizar_prato/<int:prato_id>/',visualizar_prato),
    path('adicionar_prato/',adicionarPrato),
    path('editar_prato/<int:prato_id>/',editarPrato),
    path('remover_prato/<int:prato_id>/',removerPrato),
    ##ingrediente
    path('adicionar_ingrediente/',adicionarIngrediente),
    path('editar_ingrediente/<int:id_ingrediente>/',editarIngrediente),
    path('apagar_ingrediente/<int:id_ingrediente>/',apagarIngrediente),

]