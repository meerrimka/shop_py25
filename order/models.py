import uuid
from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product



User = get_user_model()


class Order(models.Model):
    ORDER_STATUS = (('б/у', 'Б/У'),
                    ('Новый', 'Новый'))
    ORDER_COLOR = (('Синий', 'Cиний'),
                   ('Красный', 'Красный'))
    ORDER_DELIVERY = (('Бесплатная доставка', 'Бесплатная доставка'),
                      ('Платная доставка', 'Платная доставка'),
                      ('Самовывоз', 'Самовывоз'))
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=50, choices=ORDER_STATUS, null=True, blank=True)
    color = models.CharField(max_length=50, choices=ORDER_COLOR, null=True, blank=True)
    delivery = models.CharField(max_length=50, choices=ORDER_DELIVERY, null=True, blank=True)
    is_confirm = models.BooleanField(default=True)
    amount = models.PositiveIntegerField()
    addres = models.TextField()
    number = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, 
    decimal_places=2,
    default=0)                                                                    
    created_at = models.DateTimeField(auto_now_add=True)
    activation_code = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return f'{self.owner} ---> вы успешно оформили заказ'

    def save(self, *args, **kwargs):
        self.total_price = self.amount * self.product.price     #это умножает и выдает весь ответ
        return super().save(*args, **kwargs)