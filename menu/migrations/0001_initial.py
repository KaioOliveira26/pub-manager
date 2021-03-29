# Generated by Django 3.1.7 on 2021-03-26 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='assets/items')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ItemSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='menu.item')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.sale')),
            ],
        ),
    ]
