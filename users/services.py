from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    flag=0
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            # Si existe un usuario con ese nombre y contraseña
            if user is not None and user.is_active:
                # Hacemos el login manualmente
                do_login(request, user)
                #Preguntamos si es Admin
                if user.is_staff:
                    flag=1
                else:
                # En caso de que sea un empleado
                    flag=2
    #Preparamos la respuesta
    reply = {
        'flag': flag,
        'form': form
        }
    return reply

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    flag=0
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Creamos la nueva cuenta de usuario
            user = form.save()
            # Si el usuario se crea correctamente 
            if user is not None:
                do_login(request, user)
                # Y le redireccionamos a la portada
                flag=1
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    #Preparamos la respuesta
    reply = {'flag': flag, 'form': form}
    return reply