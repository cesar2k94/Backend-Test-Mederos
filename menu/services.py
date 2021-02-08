from .models import menu
from . import models
from .forms import MenuForm

def menu_double(form):
    forms=form.instance.date
    if(menu.objects.filter(date=forms)).first()==None:
        return True
    else:
        return False 

def modify(request,form,form1):
    flag=0
    date=form.cleaned_data['date']
    #Ask if there is a menu available that day
    if(models.menu.objects.filter(date=date).first()==None):
        flag=1
    else:
        instances=models.menu.objects.get(date=date)
        form1= MenuForm(instance=instances)
        if 'Guardar' in request.POST:
            form1=MenuForm(request.POST,instance=instances)
            if form1.is_valid():
                #Save the modified menu
                form1.save()
                flag=2
    reply={
        "flag":flag,
        "form1":form1
        }
    return reply
