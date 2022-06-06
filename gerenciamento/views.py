from django.shortcuts import render,redirect

# Create your views here.
def mainFrame(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        print("user not authenticated")
        return redirect ('/auth/user/login')