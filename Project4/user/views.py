from django.shortcuts import render, redirect
from hashlib import sha256
from .models import User
from ecommerce.models import Client

def login(request):
    # return render(request, 'user/templates/login.html')
    return render(request, 'registration/login.html') 

def signup(request):
    # return render(request, 'user/templates/signup.html')
    return render(request, 'registration/signup.html')

def validate_signup(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('signup-user')
    
    if len(senha) < 8:
        return redirect('signup-user')
    
    if User.objects.filter(email=email).exists():
        return redirect('signup-user')

    try:    
        senha = sha256(senha.encode()).hexdigest()
        user = User.objects.create(**{'name': nome,'email': email, 'senha': senha})
        # Client(**{'user': user, 'name': user.name, 'email': user.email}).save()
        return redirect('login')
    except:
        return redirect('signup-user')
    
def validate_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    user = User.objects.filter(email=email).filter(senha=senha).first()

    if not user:
        return redirect('login')
    else:
        request.session['user_id'] = user.pk
        request.session['user_name'] = user.name
        return redirect('home')

def logout(request):
    request.session.flush()
    return redirect('home')