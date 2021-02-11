from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(null=True,blank=True)
    digital = models.BooleanField(default=False,null=True)
    def __str__(self):
        return self.name


    @property
    def get_cart_items(self):
        ordereditems = self.orderitem_set.all()
        total = sum([item.quantity for item in ordereditems])
        return total
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        ordereditems = self.orderitem_set.all()
        total = sum([item.get_total for item in ordereditems])
        return total



    @property
    def get_cart_items(self):
        ordereditems = self.orderitem_set.all()
        total = sum([item.quantity for item in ordereditems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price*self.quantity
        return total


class ShippingAdress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    address = models.TextField(max_length=500,null=False)
    city = models.CharField(max_length=500, null=False)
    state = models.CharField(max_length=500, null=False)
    zipcode = models.CharField(max_length=500, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address









