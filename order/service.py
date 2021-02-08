from datetime import time,date
from .forms import OrderForm
from menu.forms import MenuForm
from . import models
from menu.models import menu

#Comparar hora de pedido con horario límite 
def time_now(t):
    limit=time(11,0,0)
    if limit > t:
        return True
    else:
        return False    
 
def orders(request):
    today=date.today() 
    user=request.user.id
    username=request.user.username
    form=MenuForm()
    form1=OrderForm()
    flag=0
    if(menu.objects.filter(date=today).first()==None):
        #El menú del día no está listo
        flag=1
    else:
        #Verifica si el usuario no ha solicitado el menú del día
        if(models.order.objects.filter(user_id=user).filter(created=today).first()==None):
            instances=menu.objects.get(date=today)
            form = MenuForm(instance=instances)
            if request.method=="POST":
                form1=OrderForm(request.POST)                   
                if form1.is_valid():
                    #Se realizó el pedido con éxito
                    form1.instance.user_id=user
                    form1.instance.username=username
                    lista=form1.save()
                    flag=3
                else:
                    flag=4
            else:
                flag=4
        else:
            #El usuario ya realizó su pedido
            flag=2
    reply={
        "flag":flag,
        "form":form,
        "form1":form1
        }
    return reply 