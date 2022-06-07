from email.policy import EmailPolicy
from django.core.checks import messages
from django.shortcuts import get_object_or_404, render,redirect
from accounts.forms import UserCreationForm, UserChangeForm, UserDeleteForm
from accounts.models import Account
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def SignUp(request):
    if request.method == "GET":
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request,"user/adduser.html", context=context)
    else:
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            return redirect("/")
            ##REDIRECIONAR PARA DASHBOARD
        
        context = {
                "form": form,
                
            }
    return render(request,"user/adduser.html", context=context)


def Login(request):
    return render(request,"login.html")
@login_required
def ChangeUsr(request):
        usr = request.user
        id_usr = usr.id
        post = get_object_or_404(Account, pk=id_usr)
        form = UserChangeForm(instance=post)
        if(request.method == 'POST'):
            form = UserChangeForm(request.POST,request.FILES,instance=post)
            if(form.is_valid()):
                post = form.save(commit=False)
                post.email = form.cleaned_data['email']
                post.logo = form.cleaned_data['logo']
                post.proprietario = form.cleaned_data['proprietario']
                post.nome_empresa = form.cleaned_data['nome_empresa']
                post.cnpj = form.cleaned_data['cnpj']
                post.celular = form.cleaned_data['celular']
                post.segmento_empresa = form.cleaned_data['segmento_empresa']
                post.save()
                return redirect ('/')
            
        return render(request, 'user/edit_user.html', {'form': form, 'post' : post,'logo': usr.logo,})

@login_required
def usrDelete(request):

    if request.method == "GET":
        current_user = request.user
        id_usr = current_user.email
        form = UserDeleteForm()

        context = {
            'form': form,
            'id_usr': id_usr,
        }
    else:
        try: 
            form = UserDeleteForm(request.POST)
            ## if user = request.user
            user = form['email'].value()
            u = Account.objects.get(email=user)
            u.delete()
            request.session['usuario_deletado'] = user
            return redirect ('/auth/user_deleted/')

        except:  
            return render(request, 'user/delete_error.html')
            

        
    return render(request, 'user/delete_user.html',context)

def userDeleted(request):
    if request.session['usuario_deletado']:
        return render(request, "user/user_deleted.html")