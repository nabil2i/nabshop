# Generated by Django 4.1.7 on 2023-03-14 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_bookedition_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookedition',
            options={'ordering': ['book__title']},
        ),
    ]
