from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from clientes.models import Cliente
from datetime import date
from cuentas.models import Cuenta
from prestamos.forms import PrestamosForm
from prestamos.models import Prestamo

# Create your views here.
def prestamos_inicio(request):
    if not request.user.is_authenticated:
        return redirect('../accounts/login/')
    customer_type = Cliente.objects.get(user=request.user.id).customer_type
    if request.method == 'POST':
        form = PrestamosForm(request.user.id, request.POST)
        if form.is_valid():
            loan_type = form.cleaned_data['loan_type']
            loan_total=form.cleaned_data['loan_total']
            target_account = form.cleaned_data['target_account']
            cliente = Cliente.objects.get(user=request.user.id)
            current_date = date.today()
            formatted_date = current_date.strftime("%Y-%m-%d")
            if (customer_type == 'Classic' and int(loan_total) <= 100000) or (customer_type == 'Gold' and int(loan_total) <= 300000) or (customer_type == 'Black' and int(loan_total) <= 500000):
                prestamo = Prestamo(loan_type=loan_type, loan_date = formatted_date, loan_total=loan_total, customer_id=cliente, target_account = target_account)
                prestamo.save()
                cuenta_destino = Cuenta.objects.filter(account_id=target_account.account_id)
                nuevo_saldo = int(Cuenta.objects.get(account_id=target_account.account_id).balance) + int(loan_total)
                cuenta_destino.update(balance=nuevo_saldo)
                return HttpResponseRedirect('prestamos/otorgado')
            else:
                form.add_error(None,'Loan total is over the limit for your account')
        else:
            form.add_error(None,'Invalid form')
    else:
        form = PrestamosForm(user=request.user)
    
    return render(request, 'prestamos.html', {"username": request.user.username, "form": form, "customer_type": customer_type})

def prestamo_otorgado(request):
    if not request.user.is_authenticated:
        return redirect('../accounts/login/')
    return render(request, 'prestamo-otorgado.html', {"username": request.user.username})