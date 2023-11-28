from django.db import models

# Create your models here.

class Movimientos(models.Model):
    movimiento_id = models.AutoField(primary_key=True, blank=True, null=False)
    numero_cuenta = models.IntegerField(blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    tipo_operacion = models.TextField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)
