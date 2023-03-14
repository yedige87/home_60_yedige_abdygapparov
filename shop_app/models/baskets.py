from django.db import models


class Basket(models.Model):
    type = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Тип информации: 1-итог,2-товар', default=0)
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование продукта', default='Товар')
    qty_prod = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Количество единиц в магазине', default=0)
    qty = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Количество единиц в корзине', default=0)
    qty_old = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Прежднее количество единиц в корзине', default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена продукта', default=0)
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Стоимость продукта', default=0)
    product = models.ForeignKey(
        verbose_name='Продукт',
        to='shop_app.Product',
        related_name='basket',
        null=True,
        on_delete=models.RESTRICT
    )
    customer = models.ForeignKey(
        verbose_name='Покупатель',
        to='shop_app.Customer',
        related_name='basket',
        null=True,
        on_delete=models.RESTRICT
    )