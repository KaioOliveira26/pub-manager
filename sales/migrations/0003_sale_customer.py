# Generated by Django 3.1.7 on 2021-03-29 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('sales', '0002_sale_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customer'),
            preserve_default=False,
        ),
    ]
