from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def cadastrar_usuario(request):
    if request.method == "POST":
        form_user = UserCreationForm(request.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect('listar_tarefas')
    else:
        form_user = UserCreationForm()
    return render(request, 'usuarios/form_usuario.html', {"form_user":form_user})


def logar_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('listar_tarefas')
        else:
            messages.error(request, 'Dados incorretos!')
            return redirect('login')
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form_login':form_login})

def deslogar_usuario(request):
    logout(request)
    return redirect('login')