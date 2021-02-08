from datetime import time,date
from .forms import OrderForm
from menu.forms import MenuForm
from . import models
from menu.models import menu

#Compare order time with deadline 
def time_now(t):
    limit=time(19,0,0)
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
        #The menu of the day is not ready
        flag=1
    else:
        #Check if the user has not requested the menu of the day
        if(models.order.objects.filter(user_id=user).filter(created=today).first()==None):
            instances=menu.objects.get(date=today)
            form = MenuForm(instance=instances)
            if request.method=="POST":
                form1=OrderForm(request.POST)                   
                if form1.is_valid():
                    #The order was successfully placed
                    form1.instance.user_id=user
                    form1.instance.username=username
                    lista=form1.save()
                    flag=3
                else:
                    flag=4
            else:
                flag=4
        else:
            #The user has already placed their order
            flag=2
    reply={
        "flag":flag,
        "form":form,
        "form1":form1
        }
    return reply 