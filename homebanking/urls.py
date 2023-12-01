"""
URL configuration for homebanking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from accounts.views import home
from movimientos.views import movimientos_inicio
from prestamos.views import prestamo_otorgado, prestamos_inicio
from signup.views import signup
from cuentas.views import cuenta_detalle, cuentas_inicio, agregar_cuenta
from tarjetas.views import agregar_tarjeta, tarjeta_detalle, tarjetas_inicio


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/signup/", signup , name='signup'),
    path("", home, name="home"),
    path("cuentas/", cuentas_inicio, name="cuentas"),
    path("cuentas/agregar/", agregar_cuenta, name="agregar cuenta"),
    path("cuentas/<int:account_id>/", cuenta_detalle, name="cuenta detalle"),
    path("tarjetas/", tarjetas_inicio, name="tarjetas"),
    path("tarjetas/<int:card_number>/", tarjeta_detalle, name="tarjeta detalle"),
    path("tarjetas/agregar/", agregar_tarjeta, name="agregar tarjeta"),
    path("prestamos/", prestamos_inicio, name="prestamos"),
    path("prestamos/otorgado", prestamo_otorgado, name="prestamo otorgado"),
    path("movimientos/", movimientos_inicio, name="movimientos"),
]
