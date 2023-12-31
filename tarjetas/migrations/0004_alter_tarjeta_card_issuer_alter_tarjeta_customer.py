# Generated by Django 4.2.7 on 2023-11-28 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_remove_cliente_id_cliente_customer_id'),
        ('tarjetas', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjeta',
            name='card_issuer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tarjetas.marcasdetarjeta'),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='customer',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente'),
            preserve_default=False,
        ),
    ]
