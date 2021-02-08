from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

def login(request):
    # Create the empty authentication form
    form = AuthenticationForm()
    flag=0
    if request.method == "POST":
        # Add the received data to the form
        form = AuthenticationForm(data=request.POST)       
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            # If there is a user with that name and password
            if user is not None and user.is_active:
                # Do the manual login
                do_login(request, user)
                #Ask if you are Admin
                if user.is_staff:
                    flag=1
                else:
                #In case you are an employee
                    flag=2
    #Prepare the answer
    reply = {
        'flag': flag,
        'form': form
        }
    return reply

def register(request):
    # Create the empty authentication form
    form = UserCreationForm()
    flag=0
    if request.method == "POST":
        # We add the data received to the form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            # Create the new user account
            user = form.save()
            # If the user is created successfully
            if user is not None:
                do_login(request, user)
                # Redirect to front page
                flag=1
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    #Prepare the answer
    reply = {'flag': flag, 'form': form}
    return reply