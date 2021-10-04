# Generated by Django 3.2 on 2021-09-02 12:33

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210902_1421'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and -/_ only.', max_length=100, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid username. This value may contain only letters, digits, -,_', regex='^[a-zA-Z0-9\\-_ ]{4,100}$')], verbose_name='username'),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('username', 'phone', 'email'), ('email', 'phone')},
        ),
    ]