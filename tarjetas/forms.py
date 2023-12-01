from django import forms
from django.core.exceptions import ValidationError
from .models import Tarjeta

class TarjetaForm(forms.ModelForm):
   class Meta:
       model = Tarjeta
       fields = 'card_type', 'card_issuer', 'related_account'

   def clean(self):
       cleaned_data = super().clean()
       card_type = cleaned_data.get('card_type')
       related_account = cleaned_data.get('related_account')

       if card_type == 'DEBITO' and not related_account:
           raise ValidationError("related_account is required for debito cards")
       if card_type == 'CREDITO' and related_account:
           raise ValidationError("Credit cards are not tied to a specific account")
