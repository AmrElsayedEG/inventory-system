# Generated by Django 3.2 on 2021-09-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='items_left',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
