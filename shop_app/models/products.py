from django.db import models
from django.db.models import TextChoices


class CategoryChoice(TextChoices):
    OTHER = 'other', 'Разное'
    SMARTPHOHE = 'smartphones', 'Смартфоны'
    LAPTOP = 'laptops', 'Ноутбуки'
    REFRIGERATOR = 'refrigerators', 'Холодильники'
    TV = 'TV', 'Телевизоры'


class Product(models.Model):
    category = models.CharField(choices=CategoryChoice.choices, default=CategoryChoice.OTHER, verbose_name='Категория',
                                max_length=20)
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование продукта')
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Описание продукта')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена продукта')
    photo = models.CharField(max_length=200, null=False, blank=False, verbose_name='Изображение продукта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    qty = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Остатки продукта', default=0)


def __str__(self):
    return f"Продукт: {self.title}"


class Meta:
    verbose_name = 'Товары'
    verbose_name_plural = 'Товары'
    ordering = ['category', 'title']
