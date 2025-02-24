from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserForm
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home/home.html')

@csrf_exempt
def register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('MainTM:home')
    else:
        form = CustomUserForm()
    return render(request, 'home/register.html', {'form': form})

@csrf_exempt
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('MainTM:home')
    return render(request, 'home/login.html')
