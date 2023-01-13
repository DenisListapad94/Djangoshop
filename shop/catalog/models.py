from django.db import models


class Dress_style(models.Model):
    title_style = models.CharField(max_length=100)

    def __str__(self):
        return self.title_style

    class Meta:
        verbose_name_plural = 'Стиль'


class Clothes(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(null=True, verbose_name='описание')
    price = models.FloatField(null=True, verbose_name='цена')
    size = models.IntegerField(verbose_name='размер')
    color = models.CharField(max_length=100, null=True, verbose_name='цвет')
    dress_style = models.ForeignKey('Dress_style', on_delete=models.CASCADE, null=True)
    article = models.OneToOneField('Article', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-price"]
        verbose_name_plural = 'Одежда'


class Article(models.Model):
    article = models.CharField(max_length=100)

    def __str__(self):
        return self.article

    class Meta:
        verbose_name_plural = 'Артикль'
