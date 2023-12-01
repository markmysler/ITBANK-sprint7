from django.db import models

from clientes.models import Cliente
from cuentas.models import Cuenta

# Create your models here.

class TarjetaEmisor(models.TextChoices):
       VISA = 'VISA', 'VISA'
       MASTER_CARD = 'MASTER_CARD', 'MASTER_CARD'
       AMERICAN_EXPRESS = 'AMERICAN_EXPRESS', 'AMERICAN_EXPRESS'

class TarjetaType(models.TextChoices):
       CREDITO = 'CREDITO', 'CREDITO'
       DEBITO = 'DEBITO', 'DEBITO'

class Tarjeta(models.Model):
    card_number = models.AutoField(primary_key=True, blank=True, null=False, auto_created=True)
    cvv = models.IntegerField(db_column='CVV', blank=True, null=True)  # Field name made lowercase.
    emision_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    card_type = models.CharField(
       max_length=25,
       choices=TarjetaType.choices,
       default=TarjetaType.DEBITO,
   )
    card_issuer = models.CharField(
       max_length=25,
       choices=TarjetaEmisor.choices,
       default=TarjetaEmisor.VISA,
   )
    customer_id = models.ForeignKey(Cliente, models.CASCADE, blank=True, null=False)
    related_account = models.ForeignKey(Cuenta, models.CASCADE, blank=True, null=True)

