# Generated by Django 5.0.7 on 2024-10-13 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0008_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('address_1', models.CharField(max_length=100)),
                ('address_2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
                ('county', models.CharField(blank=True, max_length=100, null=True)),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(max_length=60)),
                ('delivery_charge', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_datetime', models.DateTimeField(auto_now_add=True)),
                ('total_order_cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('product_option', models.ForeignKey(limit_choices_to={'parent__isnull': False}, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]
