# Generated by Django 5.0.7 on 2024-10-12 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_image_url_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_options',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
