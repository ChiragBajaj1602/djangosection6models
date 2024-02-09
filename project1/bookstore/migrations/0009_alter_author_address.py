# Generated by Django 5.0.2 on 2024-02-09 04:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0008_address_author_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='bookstore.address'),
        ),
    ]