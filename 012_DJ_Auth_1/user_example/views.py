from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'user_example/index.html')

@login_required
def special(request):
    return render(request, "user_example/special.html")

def register(request):
    form = UserCreationForm(request.POST or None)
    # form = UserCreationForm()
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    if form.is_valid():
            form.save()
            # that creates a new user
            # after creation of the user, want to authenticate it
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # inspect the page and see the first password is password1, import authenticate
            user = authenticate(username=username, password=password)
            
            # want user to login right after registered, import login
            login(request, user)
            # want to redirect to home page, import redirect
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, "registration/register.html", context)