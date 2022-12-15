from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Укажите категорию")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя', blank=False)
    summary = models.TextField(max_length=1000, verbose_name="Описание", blank=False)
    category = models.ForeignKey('category', verbose_name="Выбор категории", on_delete=models.CASCADE, blank=False)
    photo = models.ImageField(max_length=200, upload_to='media', blank=False, null=True, verbose_name='Фотография')