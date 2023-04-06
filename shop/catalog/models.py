from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.signals import post_save
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
        # verbose_name_plural = 'Пользователи'
        abstract = True
        # indexes = [
        #     models.Index(fields=['name'], name='name_idx'),
        #     models.Index(Lower('adress').desc(), 'name', name='lower_adress_name_idx')
        # ]


class Managers(Users):
    experiences = models.IntegerField(verbose_name='стаж', null=True)
    level_access = models.IntegerField(verbose_name='уровень допуска', null=True)

    def __str__(self):
        return self.name


class Costumers(Users):
    discont_card = models.IntegerField(verbose_name='скидка', null=True)
    orders = models.ForeignKey('Orders', on_delete=models.CASCADE, null=True)
    balance = models.FloatField(verbose_name='баланс', default=1000)
    # def __str__(self):
    #     return self.name


class Shop(models.Model):
    adress = models.CharField(max_length=50, verbose_name='адрес')
    phone = models.CharField(max_length=50, verbose_name='телефон')
    balance = models.FloatField(verbose_name='баланс', default=100000)
    photo = models.ImageField(upload_to='shop_photo', null=True, blank=True)

    orders = models.ForeignKey('Orders', on_delete=models.CASCADE, null=True)
    managers = models.ForeignKey('Managers', on_delete=models.CASCADE, null=True)

    clothes = models.ForeignKey('Clothes', on_delete=models.CASCADE, null=True)
    feedback = models.ForeignKey('Feedback', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return f"{self.adress}"


class Orders(models.Model):
    order_date = models.DateTimeField(null=True)
    clothes = models.ForeignKey('Clothes', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{self.order_date}"


class Delivery_orders(Orders):
    adress = models.CharField(max_length=100, verbose_name='aдрес доставки')
    comment = models.TextField(verbose_name="комментарий к заказу")

    def __str__(self):
        return self.adress


class Take_away_orders(Orders):
    comment = models.TextField(verbose_name="комментарий к заказу")

    def __str__(self):
        return self.shop


STATUS_CHOICES = [
    ('s', 'Sold'),
    ('a', 'Available'),
]


class Clothes(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(null=True, verbose_name='описание')
    price = models.FloatField(null=True, verbose_name='цена')
    size = models.IntegerField(verbose_name='размер')
    color = models.CharField(max_length=100, null=True, verbose_name='цвет')
    category = models.IntegerField(verbose_name='категория', null=True)
    article = models.OneToOneField('Article', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Одежда'


class Article(models.Model):
    article = models.IntegerField(verbose_name='артикул')
    serial_number = models.CharField(max_length=50, verbose_name='серийный номер')

    def __str__(self):
        return str(self.article)

    class Meta:
        verbose_name_plural = 'Артикль'


class Feedback(models.Model):
    rating = models.IntegerField(verbose_name='рейтинг')
    comment = models.TextField('комментарий')


def fun_receiver(sender, instance, created, **kwargs):
    if instance.clothes.name:
        instance.clothes.status = 's'
        # cl = Clothes.objects.get(id=instance.clothes.id)
        # cl.save()


post_save.connect(fun_receiver, sender=Orders)


class Storage(models.Model):
    value = models.CharField(max_length=100)
