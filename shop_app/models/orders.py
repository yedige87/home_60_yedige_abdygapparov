from django.db import models


class Order(models.Model):
    order_num = models.PositiveSmallIntegerField(null=True, blank=False, verbose_name='Номер заказа', default=0)
    type = models.PositiveSmallIntegerField(null=True, blank=False, verbose_name='Тип информации: 1-итог,2-товар', default=0)
    title = models.CharField(max_length=100, null=True, blank=False, verbose_name='Наименование продукта', default='Товар')
    qty = models.PositiveSmallIntegerField(null=True, blank=False, verbose_name='Остатки продукта', default=0)
    qty_old = models.PositiveSmallIntegerField(null=True, blank=False, verbose_name='Остатки продукта', default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена продукта', default=0)
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Стоимость продуктов', default=0)
    product_id = models.PositiveSmallIntegerField(null=True, blank=False, verbose_name='Id продукта', default=0)
    customer_id = models.PositiveSmallIntegerField(null=True, blank=False, verbose_name='Id клиента', default=0)