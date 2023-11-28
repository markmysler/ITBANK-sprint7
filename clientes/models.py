from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class CustomerType(models.TextChoices):
       CLASSIC = 'Classic', 'Classic'
       GOLD = 'Gold', 'Gold'
       BLACK = 'Black', 'Black'
       
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.AutoField(primary_key=True, null=False, auto_created=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    customer_type = models.CharField(
       max_length=20,
       choices=CustomerType.choices,
       default=CustomerType.CLASSIC,
   )

