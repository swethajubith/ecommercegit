# Generated by Django 4.2.3 on 2023-08-05 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecommerceapp', '0002_alter_product_options_alter_category_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartid', models.CharField(blank=True, max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Cart',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.product')),
            ],
            options={
                'db_table': 'CartItem',
            },
        ),
    ]
