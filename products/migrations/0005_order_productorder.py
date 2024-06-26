# Generated by Django 5.0.4 on 2024-05-15 21:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_department_id_departments_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField()),
                ('status', models.CharField(max_length=30)),
                ('order_type', models.CharField(choices=[('incoming', 'incoming'), ('outgoing', 'outgoing')], default='outgoing', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
            options={
                'unique_together': {('order', 'product')},
            },
        ),
    ]
