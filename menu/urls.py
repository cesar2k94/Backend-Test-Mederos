from django.urls import path
from . import views

urlpatterns = [

    path('', views.menu,name="menu"),
    path('administrator', views.administrator,name="administrator"),
    path('modify_menu', views.modify_menu, name="modify_menu"),   
]
