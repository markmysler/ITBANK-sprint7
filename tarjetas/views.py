from datetime import date, timedelta
import random
from django.shortcuts import redirect, render

from clientes.models import Cliente
from tarjetas.forms import TarjetaForm
from tarjetas.models import Tarjeta

# Create your views here.

def tarjetas_inicio(request):
    if not request.user.is_authenticated:
        return redirect('../accounts/login/')
    cliente = Cliente.objects.get(user_id = request.user.id)
    cliente_id = cliente.customer_id
    tarjetas = Tarjeta.objects.filter(customer_id=cliente_id)
    return render(request, 'tarjetas.html', {"username": request.user.username, "tarjetas": tarjetas})

def agregar_tarjeta(request):
    if not request.user.is_authenticated:
        return redirect('../../accounts/login/')
    if request.method == 'POST':
        form = TarjetaForm(request.POST)
        if form.is_valid():
            current_date = date.today()
            formatted_date = current_date.strftime("%Y-%m-%d")
            exp_date=current_date+timedelta(days=(5*365.24))
            cliente = Cliente.objects.get(user=request.user)
            tarjeta = Tarjeta(customer_id= cliente, card_type=form.cleaned_data.get('card_type'), cvv = random.randint(10**2, 10**3 - 1), emision_date=formatted_date, expiry_date=exp_date, card_issuer=form.cleaned_data.get('card_issuer'), related_account=form.cleaned_data.get('related_account'))
            tarjeta.save()
            return redirect('../')
    else:
        form = TarjetaForm()
    return render(request, 'crear-tarjeta.html', {"username": request.user.username,"form": form})
    
def tarjeta_detalle(request, card_number):
    if not request.user.is_authenticated:
        return redirect('../../accounts/login/')
    tarjeta = Tarjeta.objects.get(card_number=card_number)
    return render(request, 'tarjeta-detalle.html', {"username": request.user.username, "tarjeta": tarjeta})