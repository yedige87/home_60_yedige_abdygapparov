from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Имя покупателя')
    phone = models.CharField(max_length=20, null=False, blank=False, verbose_name='Телефон покупателя')
    address = models.CharField(max_length=40, null=False, blank=False, verbose_name='Адрес покупателя')
    products = models.ManyToManyField(
        to='shop_app.Product',
        related_name='customer',
        blank=True
    )