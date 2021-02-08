from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .service import time_now,orders
from datetime import datetime,time

# Create your views here.
@login_required(login_url="/login")
def order(request):
    t=datetime.now().time()                                                                                                                                                                                                                                    
    if time_now(t):
        reply=orders(request)
        if reply['flag']==1:
            return render(request,"sorry.html")
        else:
            if reply['flag']==2:
                return render(request,"double.html")
            else: 
                if reply['flag']==4:
                    #Place the order
                    return render(request,"order.html",
                                 {'form': reply['form'], 
                                 'form1':reply['form1']}
                                 )
                else:                  
                    if reply['flag']==3:
                        return render(request,"done.html")  
    else:
        #It's after 11 am
        return render(request,"late.html")