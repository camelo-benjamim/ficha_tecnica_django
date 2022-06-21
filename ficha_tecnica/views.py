from tracemalloc import get_object_traceback
from webbrowser import get
from django.shortcuts import render,redirect
from ficha_tecnica.models import *
from django.shortcuts import get_object_or_404
from ficha_tecnica.forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def mainView(request):
    user_status = request.user.is_authenticated
    if user_status == True:
        status = 'y'
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
    else:
        status = 'n'
        context = {
            'status': status,
        }
    
   
    
    return render(request, 'index.html', context=context)

##pratos
@login_required
def visualizar_prato(request,prato_id):
    prato = get_object_or_404(Prato,id=prato_id,usuario=request.user)
    request.session['prato_id'] = prato.id
    nome_do_prato = prato.nome_do_prato
    ingredientes = Ingredientes.objects.filter(prato=prato)
    quant_total_ingredientes = 0
    custo_total = 0
    for ingrediente in ingredientes:
        preco_unitario = ingrediente.preco_unitario
        quantidade_bruta = ingrediente.quantidade_bruta / 1000
        custo_ingrediente = preco_unitario * quantidade_bruta
        custo_total += custo_ingrediente
        quant_total_ingredientes += 1
    ##fixing error by 0 division
    ##consertando erro de divisão por 0
    try:
        custo_total = round(custo_total,2)
        lucro = float(prato.preco_de_venda) - float(custo_total)
        lucro = round(lucro,2)
        preco_de_venda = round(prato.preco_de_venda, 2)
        cmv = (preco_de_venda - custo_total) / custo_total
        cmv = round(cmv,2) * 100
    except:
        custo_total = 0
        lucro = 0
        preco_de_venda = round(prato.preco_de_venda,2)
        cmv = 0


    context = {'ingredientes': ingredientes,'custo_total': custo_total,'lucro': lucro, 'cmv': cmv,'nome_do_prato': nome_do_prato,'quant_total_ingredientes': quant_total_ingredientes,}
    return render(request,'ficha_tecnica/pratos/visualizar_prato.html',context=context)

@login_required
def adicionarPrato(request):
    if request.method == "GET":
        form = FormPrato()
    else:
        form = FormPrato(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
    context = {
        'form': form,
    }
    return render(request,'ficha_tecnica/pratos/adicionar_prato.html',context=context)
@login_required
def editarPrato(request,prato_id):
    prato = get_object_or_404(Prato,id=prato_id,usuario=request.user)
    form = FormPrato(instance=prato)
    if request.method == "POST":
        form = FormPrato(request.POST,instance=prato)
        if form.is_valid():
            post = form.save(commit=False)
            post.nome_do_prato = form.cleaned_data['nome_do_prato']
            post.tamanho_receita = form.cleaned_data['tamanho_receita']
            post.classificacao_tamanho = form.cleaned_data['classificacao_tamanho']
            post.preco_de_venda = form.cleaned_data['preco_de_venda']
            post.save()
            return redirect('../../')
    context = {
        'form':form,
        }
    return render(request,'ficha_tecnica/pratos/editar_prato.html',context=context)
@login_required
def removerPrato(request,prato_id):
    prato = get_object_or_404(Prato,id=prato_id,usuario=request.user)
    prato.delete()
    return redirect('../../')
##ingredientes
@login_required
def adicionarIngrediente(request):
    id_usr = request.user.id
    if request.method == "GET":
        form = FormIngredientes(id_usr)
    else:
        form = FormIngredientes(id_usr,request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/visualizar_prato/' + str(request.session['prato_id']) + '/')
    context = {
        'form': form,
    }
    return render(request,'ficha_tecnica/ingredientes/adicionar_ingrediente.html',context=context)
@login_required
def editarIngrediente(request,id_ingrediente):
    id_usr = request.user.id
    prato = get_object_or_404(Prato,id=request.session['prato_id'],usuario=request.user)
    ingrediente = get_object_or_404(Ingredientes,prato=prato,id=id_ingrediente)
    form = FormIngredientes(instance=ingrediente,id_usr=id_usr)
    if request.method == "POST":
        form = FormIngredientes(id_usr,request.POST,instance=ingrediente)
        if form.is_valid():
            post = form.save(commit=False)
            post.prato = form.cleaned_data['prato']
            post.nome_ingrediente = form.cleaned_data['nome_ingrediente']
            post.classificar_tamanho = form.cleaned_data['classificar_tamanho']
            post.quantidade_bruta = form.cleaned_data['quantidade_bruta']
            post.quantidade_liquida = form.cleaned_data['quantidade_liquida']
            post.preco_unitario = form.cleaned_data['preco_unitario']
            post.save()
            return redirect('../../visualizar_prato/' + str(request.session['prato_id']) + '/')
    context = {
        'form':form,
    }
    return render(request,'ficha_tecnica/ingredientes/editar_ingrediente.html',context=context)
@login_required
def apagarIngrediente(request,id_ingrediente):
    ingrediente = get_object_or_404(Ingredientes, id=id_ingrediente)
    prato = ingrediente.prato
    if prato.usuario == request.user:
        ingrediente.delete()
        id_prato = request.session['prato_id']
        return redirect('/visualizar_prato/{}/'.format(str(id_prato)))