from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"  
    
def home(req):
    if not req.user.is_authenticated:
        return redirect('accounts/login/')
    return render(req, 'home.html', {"username": req.user.username})
