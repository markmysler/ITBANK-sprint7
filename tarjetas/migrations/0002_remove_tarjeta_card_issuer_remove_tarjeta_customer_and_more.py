# Generated by Django 4.2.7 on 2023-11-27 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarjetas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarjeta',
            name='card_issuer',
        ),
        migrations.RemoveField(
            model_name='tarjeta',
            name='customer',
        ),
        migrations.DeleteModel(
            name='MarcasDeTarjeta',
        ),
        migrations.DeleteModel(
            name='Tarjeta',
        ),
    ]
