from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from app.managers import CustomUserManager
import uuid


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class FoodItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name= models.CharField(max_length=100, blank=False)
    description= models.TextField(max_length=250, blank=False)
    price= models.DecimalField(max_digits=6, decimal_places=2)
    created_by = models.ForeignKey('app.CustomUser', related_name='fooditems', on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True, editable=False)
    image_url = models.URLField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.name} @ {self.price}"

class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    orderid = models.ForeignKey('app.Order', related_name='orderitems', on_delete=models.DO_NOTHING)
    fooditemid = models.ForeignKey('app.FoodItem', related_name='fooditemid', on_delete=models.DO_NOTHING, blank=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.fooditemid.name} for {self.orderid}"
    
    @property
    def total_price(self):
        return self.quantity * self.fooditemid.price
    
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_by = models.ForeignKey('app.CustomUser', related_name='orders', on_delete=models.CASCADE)
    order_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return f"Order By {self.order_by} @ {self.order_at}"
    

    @property
    def total_price(self):
        print("Calculating Total Price of Order. Step 1 Get all Order related Items")
        related_order_items = OrderItem.objects.filter(orderid__id=self.id)
        sum = 0
        for orderitem in related_order_items:
            sum += orderitem.total_price
        return sum