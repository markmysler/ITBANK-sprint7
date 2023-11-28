from django.db import models

# Create your models here.
class TiposDeCuenta(models.Model):
    account_type = models.TextField(primary_key=True, blank=True, null=False)
    option_number = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True, null=False)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    account_type = models.TextField(blank=True, null=True)
