# Generated by Django 3.1.7 on 2021-03-30 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='telefone',
            new_name='phone',
        ),
    ]
