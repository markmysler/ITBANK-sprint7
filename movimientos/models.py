from django.db import models

from cuentas.models import Cuenta

# Create your models here.

class Movimiento(models.Model):
    movimiento_id = models.AutoField(primary_key=True, blank=True, null=False, auto_created=True)
    cuenta_origen = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='transferencias_salientes')
    cuenta_destino = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='transferencias_entrantes')
    monto = models.FloatField(blank=True, null=True)
    tipo_operacion = models.TextField(blank=True, null=True)
    fecha_hora = models.DateTimeField(blank=True, null=True)
