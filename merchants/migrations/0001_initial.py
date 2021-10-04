# Generated by Django 3.2 on 2021-09-02 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalePoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('coordinates', models.JSONField(blank=True, null=True)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'salepoint',
                'verbose_name_plural': 'salepoints',
                'db_table': 'salepoint',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('coordinates', models.JSONField(blank=True, null=True)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'supplier',
                'verbose_name_plural': 'suppliers',
                'db_table': 'supplier',
            },
        ),
    ]
