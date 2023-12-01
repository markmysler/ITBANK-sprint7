from django import forms
from clientes.models import Cliente

from cuentas.models import Cuenta

from .models import Prestamo, PrestamoType


class PrestamosForm(forms.ModelForm):
    target_account = forms.ModelChoiceField(queryset=Cuenta.objects.none())
    class Meta:
        model = Prestamo
        fields = ['loan_type', 'loan_total', 'target_account']
    def __init__(self, user, *args, **kwargs):
       super(PrestamosForm, self).__init__(*args, **kwargs)
       cliente = Cliente.objects.get(user=user)
       self.fields['target_account'].queryset = Cuenta.objects.filter(customer_id=cliente.customer_id)