# Generated by Django 5.0.2 on 2024-02-09 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0009_alter_author_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='publications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Rasta', 'verbose_name_plural': 'Address Entries'},
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('publictaions', models.ManyToManyField(to='bookstore.publications')),
            ],
        ),
    ]