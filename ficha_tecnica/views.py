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
        context = {
        'status': status,
        'pratos': pratos_usuario,
        'quant_pratos': contador_pratos,
                  }
    
    return render(request, 'index.html', context=context)

def adicionarPrato(request):
    context = {
        'a': 'a'
    }
    return render(request,'ficha_tecnica/pratos/adicionar_prato.html',context=context)