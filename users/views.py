from django.shortcuts import render,redirect
from django.contrib.auth import logout as do_logout
from . import services



def welcome(request):
    if request.user.is_authenticated:
        return render(request, "welcome.html")
    return redirect('/login')

def register(request):
    reply=services.register(request)
    if reply['flag']==1:
        return redirect ('/')
    else:
        return render(request, "register.html", {'form': reply['form']})
  
def login(request):
    #Llamamos a la función login de services
    reply=services.login(request)
    if reply['flag']==1:
        #En caso que sea el administrador
        return redirect("/menu/administrator")
    else:
        if reply['flag']==2:
            # En caso de que sea un empleado
            return redirect('/')
        else:
            return render(request, "login.html", {'form': reply['form']})

def logout(request):
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')