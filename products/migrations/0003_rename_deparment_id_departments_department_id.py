# Generated by Django 5.0.4 on 2024-05-15 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_departments_options_alter_products_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='deparment_id',
            new_name='department_id',
        ),
    ]