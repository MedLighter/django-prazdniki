from django.db import models
from users.models import User

# Create your models here.
class Orders(models.Model):
    user_id = models.ForeignKey(User, verbose_name='Заказчик', on_delete=models.PROTECT)
    order_description = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Application(models.Model):
    user_id = models.ForeignKey(User, verbose_name='Заказчик', on_delete=models.PROTECT)
    customer_name = models.CharField(max_length=100)
    customer_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Catalogs(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Каталог'

class Order_info(models.Model):
    order_id = models.ForeignKey(Orders, verbose_name='Заказ', on_delete=models.PROTECT)
    catalog_id = models.ForeignKey(Catalogs, verbose_name='Программы', on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Информация о заказах'
