from django.shortcuts import render,redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .forms import MenuForm, ModifyForm
from order.forms import OrderForm
from order import models
from order.models import order
from datetime import date
from . import models
from .services import menu_double,modify

# Create your views here.

@login_required(login_url="/login")
@staff_member_required(login_url="/login")
def menu(request):
    form=MenuForm()
    if request.method=="POST":
        form=MenuForm(request.POST)
        if form.is_valid():
            if menu_double(form):
                #Guardar el menú 
                lists=form.save(commit=False)
                lists.save()
                return render(request,"good.html")
            else:
                #En ese día ya hay menú
                return render(request,"menu_double.html")    
    return render(request,"menu.html",{'form':form})

@login_required(login_url="/login")
@staff_member_required(login_url="/login")
def administrator(request):
    today=date.today()
    #Pedidos del día
    form=order.objects.filter(created=today)
    #Menú del día
    form1=models.menu.objects.filter(date=today)
    return render(request,"administrator.html", {'forms':form,'form1':form1})

@login_required(login_url="/login")
@staff_member_required(login_url="/login")
def modify_menu(request):
    form=ModifyForm()
    if request.method=="POST":
        form=ModifyForm(request.POST)
        form1=MenuForm()
        if form.is_valid():
            reply=modify(request,form,form1)
            if reply['flag']==1:
                #No hay menú disponible para ese día
                return render(request,"exists.html")                
            else:
                if reply['flag']==2:
                    #Se modificó el menú
                    return render(request,"good.html")
                return render(request,"modify_menu.html",
                            {'form':form, 'form1':reply['form1']})
    return render(request,"modify_menu.html", {'form': form})



