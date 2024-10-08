# accounts/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
import os
from django.conf import settings


def login_view(request):
    if request.method == "POST":
        username_or_email = request.POST.get("username", None)
        password = request.POST.get("password", None)

        # Verificar se username_or_email não é None
        if username_or_email is not None:
            # Verificar se o input é um email
            if "@" in username_or_email:
                try:
                    user = User.objects.get(email=username_or_email)
                    username = user.username  # Pega o username relacionado ao email
                except User.DoesNotExist:
                    username = None
            else:
                username = username_or_email

            # Autenticar com username
            user = authenticate(request, username=username, password=password)
            print(f"Authenticated User: {user}")  # Adicione isso para depuração

            if user is not None:
                login(request, user)
                messages.success(request, "Login efetuado com sucesso!")
                return redirect("index")
            else:
                messages.error(request, "Credenciais inválidas")
                return render(
                    request, "accounts/login.html", {"error": "Credenciais inválidas"}
                )
        else:
            messages.error(request, "Nome de usuário ou e-mail não fornecido")
            return render(
                request,
                "accounts/login.html",
                {"error": "Nome de usuário ou e-mail não fornecido"},
            )

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect("login")


def register_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecionar para uma página após o registro
            return redirect("login")
        else:
            print(form.errors)  # Isso ajudará a depurar possíveis erros
    else:
        form = UserForm()
    return render(request, "accounts/register.html", {"form": form})


# robots google
def robots(request):
    if not settings.DEBUG:
        path = os.path.join(settings.STATIC_ROOT, 'robots.txt') # producao
    else:
        path = os.path.join(settings.BASE_DIR, 'core/static/robots.txt') # desenvolvimento
        
    with open(path, 'r') as arquivo:
        return HttpResponse(arquivo, content_type="text/plain")
        
    #print(path)     
        #return HttpResponse(arq, content_type="text/plain")
    # return HttpResponse("teste")
