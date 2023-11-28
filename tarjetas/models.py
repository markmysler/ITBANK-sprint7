from django.db import models

from clientes.models import Cliente

# Create your models here.

class MarcasDeTarjeta(models.Model):
    card_issuer = models.TextField(primary_key=True, blank=True, null=False)
    option_number = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.



class Tarjeta(models.Model):
    card_number = models.TextField(primary_key=True, blank=True, null=False)
    cvv = models.TextField(db_column='CVV', blank=True, null=True)  # Field name made lowercase.
    emision_date = models.TextField(blank=True, null=True)
    expiry_date = models.TextField(blank=True, null=True)
    card_type = models.TextField(blank=True, null=True)
    card_issuer = models.ForeignKey(MarcasDeTarjeta, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Cliente, models.CASCADE, blank=True, null=False)

