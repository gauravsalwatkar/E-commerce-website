# Generated by Django 3.1.1 on 2021-03-16 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210316_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sub_category',
            new_name='subcategory',
        ),
    ]
