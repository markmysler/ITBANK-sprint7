from django.shortcuts import redirect, render

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from .forms import ClienteForm

def signup(request):
   if request.method == 'POST':
       user_form = UserCreationForm(request.POST)
       cliente_form = ClienteForm(request.POST)
       if user_form.is_valid() and cliente_form.is_valid():
           user = user_form.save()
           cliente = cliente_form.save(commit=False)
           cliente.user = user
           cliente.save()
           return redirect('home')
   else:
       user_form = UserCreationForm()
       cliente_form = ClienteForm()
   return render(request, 'registration/signup.html', {'user_form': user_form, 'cliente_form': cliente_form})
