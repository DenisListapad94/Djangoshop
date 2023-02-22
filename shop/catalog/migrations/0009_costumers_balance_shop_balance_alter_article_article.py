# Generated by Django 4.1.4 on 2023-01-25 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_managers_experiences_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumers',
            name='balance',
            field=models.FloatField(default=1000, verbose_name='баланс'),
        ),
        migrations.AddField(
            model_name='shop',
            name='balance',
            field=models.FloatField(default=100000, verbose_name='баланс'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article',
            field=models.IntegerField(verbose_name='артикул'),
        ),
    ]