# Generated by Django 4.1.4 on 2023-01-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_costumers_options_alter_managers_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managers',
            name='experiences',
            field=models.IntegerField(null=True, verbose_name='стаж'),
        ),
        migrations.AlterField(
            model_name='managers',
            name='level_access',
            field=models.IntegerField(null=True, verbose_name='уровень допуска'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_date',
            field=models.DateTimeField(null=True),
        ),
    ]
