from datetime import datetime
import random
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from clientes.models import Cliente
from cuentas.forms import CuentaForm, TransferenciaForm
from cuentas.models import Cuenta
from django.contrib import messages

from movimientos.models import Movimiento

# Create your views here.

def cuentas_inicio(request):
    if not request.user.is_authenticated:
        return redirect('../accounts/login/')
    cliente = Cliente.objects.get(user_id = request.user.id)
    cliente_id = cliente.customer_id
    cuentas = Cuenta.objects.filter(customer_id=cliente_id)
    
    return render(request, 'cuentas.html', {"username": request.user.username, "cuentas": cuentas})

def agregar_cuenta(request):
    if not request.user.is_authenticated:
        return redirect('../../accounts/login/')
    if request.method == 'POST':
       form = CuentaForm(request.POST)
       if form.is_valid():
           cliente = Cliente.objects.get(user=request.user)
           cuenta = Cuenta(customer_id= cliente, account_type=form.cleaned_data.get('account_type'), balance=0, iban=random.randint(10**9, 10**10 - 1))
           cuenta.save()
           return redirect('../cuentas')
    else:
        form = CuentaForm()
        return render(request, 'crear-cuenta.html', {"username": request.user.username,"form": form})
    
def cuenta_detalle(request, account_id):
    if not request.user.is_authenticated:
        return redirect('../../accounts/login/')
    if request.method == 'POST':
        form = TransferenciaForm(request.POST)
        monto = int(form.data.get('monto'))
        iban = int(form.data.get('iban'))
        cuenta = Cuenta.objects.get(account_id=account_id)
        if cuenta.balance >= monto:
            exists = Cuenta.objects.filter(iban=iban).exists()
            if exists:
                if iban != int(cuenta.iban):
                    if monto > 0:
                        saldo_actualizado_origen = cuenta.balance - monto
                        Cuenta.objects.filter(account_id=account_id).update(balance = saldo_actualizado_origen)
                        cuenta_destino = Cuenta.objects.get(iban=iban)
                        nuevo_saldo_destino = cuenta_destino.balance + monto
                        Cuenta.objects.filter(iban=iban).update(balance= nuevo_saldo_destino)
                        current_date = datetime.now()
                        movimiento = Movimiento(cuenta_origen=cuenta, cuenta_destino=cuenta_destino, monto=monto, fecha_hora=current_date, tipo_operacion='TRANSFERENCIA')
                        movimiento.save()
                    else:
                        form.add_error(None,'Ammount must be over 0')
                else:
                    form.add_error(None,'Cannot transfer funds to yourself')
            else:
                form.add_error(None,'Account not found')
        else:
            form.add_error(None,'Insufficient balance')
    else:
        form = TransferenciaForm()
        cuenta = Cuenta.objects.get(account_id=account_id)
    return render(request, 'cuenta-detalle.html', {'username': request.user.username,'cuenta': cuenta, 'form': form})