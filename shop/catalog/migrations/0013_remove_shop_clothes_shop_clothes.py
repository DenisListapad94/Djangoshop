# Generated by Django 4.1.4 on 2023-02-01 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_remove_orders_clothes_orders_clothes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='clothes',
        ),
        migrations.AddField(
            model_name='shop',
            name='clothes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.clothes'),
        ),
    ]
