from django.shortcuts import redirect, render
from clientes.models import Cliente
from django.db.models import Q
from cuentas.models import Cuenta
from movimientos.models import Movimiento

# Create your views here.

def movimientos_inicio(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')
    customer_id = Cliente.objects.get(user = request.user).customer_id
    cuentas = Cuenta.objects.filter(customer_id=customer_id).values_list('account_id', flat=True)
    cuentas_list = cuentas[::1]
    movimientos = Movimiento.objects.filter(Q(cuenta_origen__in=cuentas_list) | Q(cuenta_destino__in=cuentas_list))
    return render(request, 'movimientos.html', {"username": request.user.username, "movimientos": movimientos, "cuentas": cuentas_list})