# Generated by Django 4.1.4 on 2023-02-01 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_remove_shop_clothes_shop_clothes'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='status',
            field=models.CharField(choices=[('s', 'Sold'), ('a', 'Available')], max_length=1, null=True),
        ),
    ]
