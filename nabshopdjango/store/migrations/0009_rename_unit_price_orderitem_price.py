# Generated by Django 4.1.7 on 2023-03-20 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_orderitem_unit_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='unit_price',
            new_name='price',
        ),
    ]
