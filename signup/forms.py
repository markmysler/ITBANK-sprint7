from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from clientes.models import Cliente

class ClienteForm(forms.ModelForm):
   customer_name = forms.CharField(max_length=20, label='Name')
   customer_surname = forms.CharField(max_length=20, label='Last Name')
   customer_dni = forms.DecimalField(max_digits=8, decimal_places=0, label='DNI')
   dob = forms.DateField(input_formats=['%Y-%m-%d', '%d-%m-%Y'],widget=forms.DateInput(), label='Date of birth')    
   
   class Meta:
       model = Cliente
       fields =('customer_name', 'customer_surname', 'customer_dni', 'customer_type', 'dob')
