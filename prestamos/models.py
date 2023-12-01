from django.db import models

from clientes.models import Cliente
from cuentas.models import Cuenta

# Create your models here.

class PrestamoType(models.TextChoices):
       HIPOTECARIO = 'HIPOTECARIO', 'HIPOTECARIO'
       PERSONAL = 'PERSONAL', 'PERSONAL'
       PRENDARIO = 'PRENDARIO', 'PRENDARIO'
       

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True, null=False)
    loan_type =  models.CharField(
       max_length=20,
       choices=PrestamoType.choices,
       default=PrestamoType.PERSONAL,
   )
    loan_date = models.DateField()
    loan_total = models.IntegerField()
    customer_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    target_account = models.ForeignKey(Cuenta, on_delete=models.CASCADE)

