# Generated by Django 3.2 on 2021-09-04 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210902_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and -/_ only.', max_length=100, null=True, unique=True, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_user_worker', to=settings.AUTH_USER_MODEL),
        ),
    ]