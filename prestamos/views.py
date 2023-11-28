from django.shortcuts import redirect, render

# Create your views here.
def prestamos_inicio(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')
    return render(request, 'prestamos.html', {"username": request.user.username})