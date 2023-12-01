from django.db import models

from clientes.models import Cliente

# Create your models here.
class CuentaType(models.TextChoices):
       CAJA_AHORRO_PESOS = 'CAJA_AHORRO_PESOS', 'CAJA_AHORRO_PESOS'
       CAJA_AHORRO_DOLARES = 'CAJA_AHORRO_DOLARES', 'CAJA_AHORRO_DOLARES'
       CUENTA_CORRIENTE_PESOS = 'CUENTA_CORRIENTE_PESOS', 'CUENTA_CORRIENTE_PESOS'
       CUENTA_CORRIENTE_DOLARES = 'CUENTA_CORRIENTE_DOLARES', 'CUENTA_CORRIENTE_DOLARES'
       CUENTA_INVERSION = 'CUENTA_INVERSION', 'CUENTA_INVERSION'
       
class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True, null=False)
    customer_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    balance = models.IntegerField()
    iban = models.TextField()
    account_type = models.CharField(
       max_length=25,
       choices=CuentaType.choices,
       default=CuentaType.CAJA_AHORRO_PESOS,
   )
    def __str__(self):
       return f"Cuenta n°{self.account_id} - {" ".join(self.account_type.split('_'))}"
