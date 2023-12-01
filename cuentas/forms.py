from django import forms

from cuentas.models import Cuenta


class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['account_type']
        
class TransferenciaForm(forms.Form):
    monto = forms.IntegerField(label='Monto')
    iban = forms.IntegerField(label='IBAN')