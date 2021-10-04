# Generated by Django 3.2 on 2021-09-05 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0002_supplier_category'),
        ('delivery', '0005_remove_outproduct_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salepointdelivery',
            name='delivery_date',
        ),
        migrations.RemoveField(
            model_name='salepointdelivery',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='salepointdelivery',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='salepointdelivery',
            name='sale_point',
        ),
        migrations.AddField(
            model_name='outproduct',
            name='count_left',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='outproduct',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='outdelivery',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('canceled', 'Canceled'), ('delivered', 'Delivered')], default='pending', max_length=20),
        ),
        migrations.CreateModel(
            name='SalePointInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('cash', 'Cash'), ('postpaid', 'Postpaid')], max_length=10)),
                ('paid', models.BooleanField(default=False)),
                ('delivery_date', models.DateTimeField(auto_now=True)),
                ('delivery_items', models.ManyToManyField(to='delivery.SalePointDelivery')),
                ('sale_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchants.salepoint')),
            ],
        ),
    ]
