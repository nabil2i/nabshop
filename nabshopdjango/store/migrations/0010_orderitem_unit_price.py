# Generated by Django 4.1.7 on 2023-03-20 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_unit_price_orderitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
    ]