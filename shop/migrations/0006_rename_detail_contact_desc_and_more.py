# Generated by Django 5.1.3 on 2024-11-11 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_products_product_orders_phone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='detail',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='lastname',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='title',
            new_name='phone',
        ),
    ]
