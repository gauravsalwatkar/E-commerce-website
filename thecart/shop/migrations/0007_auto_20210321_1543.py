# Generated by Django 3.1.1 on 2021-03-21 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
