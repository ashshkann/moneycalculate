from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from .forms import Login_form


def money_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    formlogin = Login_form(request.POST or None)
    if formlogin.is_valid():
        user_name = formlogin.cleaned_data.get('username')
        password = formlogin.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/todo-list/')
        else:
            formlogin.add_error('username', 'username or password is not valid')


    context= {
        "form": formlogin
    }
    return render(request, 'loginpage.html', context)


def log_out(request):
    logout(request)
    return redirect('/login')