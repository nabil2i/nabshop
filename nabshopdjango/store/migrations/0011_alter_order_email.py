# Generated by Django 4.1.7 on 2023-03-20 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_orderitem_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=255),
        ),
    ]