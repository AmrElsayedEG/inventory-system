# Generated by Django 3.2 on 2021-09-02 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, max_length=100, null=True, unique=True, verbose_name='username'),
        ),
    ]
