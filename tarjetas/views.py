from django.shortcuts import redirect, render

# Create your views here.

def tarjetas_inicio(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')
    return render(request, 'tarjetas.html', {"username": request.user.username})