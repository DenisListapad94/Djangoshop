# Generated by Django 4.1.4 on 2023-01-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_clothes_options_remove_delivery_orders_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='costumers',
            options={},
        ),
        migrations.AlterModelOptions(
            name='managers',
            options={},
        ),
        migrations.RemoveField(
            model_name='shop',
            name='main_manager',
        ),
        migrations.AlterField(
            model_name='costumers',
            name='discont_card',
            field=models.IntegerField(null=True, verbose_name='скидка'),
        ),
    ]
