from django.shortcuts import render
from ficha_tecnica.models import *

# Create your views here.
def mainView(request):
    user_status = request.user.is_authenticated
    if user_status == True:
        status = 'y'
    else:
        status = 'n'
    
    usuario = request.user
    pratos_usuario = Prato.objects.filter(usuario=usuario)
    contador_pratos = 0
    for i in pratos_usuario:
        contador_pratos += 1
    if contador_pratos == 0:
        context = context = {
        'status': status,
                            }
    else:
        if contador_pratos == 1:
            matriz = "uni"
        else:
            if contador_pratos % 3 == 0:
                matriz = "te"
            elif contador_pratos % 2 == 0:
                matriz = "dune"
        context = {
        'status': status,
        'pratos': pratos_usuario,
        'quant_pratos': contador_pratos,
        'matriz': matriz,
                  }
    
    return render(request, 'index.html', context=context)
