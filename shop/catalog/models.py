from django.db import models
from django.db.models.functions import Lower


class Users(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    surname = models.CharField(max_length=100, verbose_name='фамилия')
    age = models.IntegerField(verbose_name='возраст')
    phone = models.CharField(max_length=50, verbose_name='телефон')
    adress = models.CharField(max_length=50, verbose_name='адрес')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Пользователи'
        indexes = [
            models.Index(fields=['name'], name='name_idx'),
            models.Index(Lower('adress').desc(), 'name', name='lower_adress_name_idx')
        ]


class Shop(models.Model):
    adress = models.CharField(max_length=50, verbose_name='адрес')
    phone = models.CharField(max_length=50, verbose_name='телефон')
    main_manager = models.CharField(max_length=50, verbose_name='Главный менеджер')

    clothes = models.ManyToManyField('Clothes')

    class Meta:
        verbose_name_plural = 'Магазины'


class Orders(models.Model):
    order_date = models.DateTimeField()
    user = models.ForeignKey('Users', on_delete=models.CASCADE, null=True)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=True)

    clothes = models.ManyToManyField('Clothes')
    class Meta:
        verbose_name_plural = 'Заказы'

class Clothes(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(null=True, verbose_name='описание')
    price = models.FloatField(null=True, verbose_name='цена')
    size = models.IntegerField(verbose_name='размер')
    color = models.CharField(max_length=100, null=True, verbose_name='цвет')

    article = models.OneToOneField('Article', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-price"]
        verbose_name_plural = 'Одежда'

class Article(models.Model):
    article = models.IntegerField(verbose_name='артикль')
    serial_number = models.CharField(max_length=50,verbose_name='серийный номер')
    def __str__(self):
        return self.article

    class Meta:
        verbose_name_plural = 'Артикль'
