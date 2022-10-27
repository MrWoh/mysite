# Generated by Django 4.0.6 on 2022-07-18 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_manager', '0002_remove_products_amount_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Price'),
        ),
    ]