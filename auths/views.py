from django.shortcuts import render, get_object_or_404, redirect
from auths.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='auths:login')
def home(request):
    return render(request, "index.html")


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('auths:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password1')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('auths:home')
            else:
                messages.info(request, 'username OR password is not valid')

        form = UserForm
        return render(request, "login.html", {'form': form})


def logoutuser(request):
    logout(request)
    return redirect('auths:login')


def register(request):
    if request.user.is_authenticated:
        return redirect('auths:home')
    else:
        form = UserForm()

        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'account has been created for ' + user)
                return redirect('auths:login')

        context = {'form': form}
        return render(request, "register.html", context)
