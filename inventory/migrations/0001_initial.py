# Generated by Django 3.2 on 2021-09-02 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boxs', models.PositiveBigIntegerField()),
                ('box_items', models.PositiveBigIntegerField()),
                ('box_price', models.PositiveIntegerField(blank=True, null=True)),
                ('item_price', models.PositiveIntegerField(blank=True, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('arrival_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'inventory',
                'verbose_name_plural': 'inventories',
                'db_table': 'inventory',
            },
        ),
    ]
