from django import urls
from django.db.models.fields import CharField 
from django.urls.conf import path, include
from ficha_tecnica.views import *


urlpatterns = [
    path('', mainView),

]