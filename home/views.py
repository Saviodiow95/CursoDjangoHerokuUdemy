from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def sair(request):
    logout(request)
    return redirect('home')