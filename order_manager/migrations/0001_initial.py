# Generated by Django 4.0.6 on 2022-07-18 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0001_initial'),
        ('supplier_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=25)),
                ('is_added', models.BooleanField(default=False)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_profile.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='Product', max_length=50, verbose_name='Product name')),
                ('amount', models.IntegerField(default='0')),
                ('unit', models.CharField(choices=[('a', 'Units'), ('b', 'Kg'), ('c', 'G'), ('d', 'L')], default='a', max_length=1, verbose_name='Unit')),
                ('order_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='Code')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_supplier', to='supplier_manager.supplier')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_added', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date_ordered', models.DateTimeField(null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order_manager.order')),
                ('product', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order_manager.products')),
            ],
        ),
    ]
