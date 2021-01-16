from django.db import models
from decimal import Decimal
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=250)
    
    class Meta:
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=250)
    
    class Meta:
        verbose_name_plural = "Product Tags"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tags, related_query_name="tags")
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    initial_qty = models.IntegerField(default=0)
    img = models.ImageField(upload_to='product-images/')

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = [
        (1, "Completed"),
        (2, "Pending"),
        (3, "Cancelled"),
    ]
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(default=2, choices=STATUS)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    @property
    def order_items_total_cost(self):
        return sum([item.item_price for item in self.orderitem_set.all()])

    @property
    def order_items_count(self):
        return sum([item.quantity for item in self.orderitem_set.all()])

    @property
    def order_items(self):
        return self.orderitem_set.all()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)

    @property
    def item_price(self):
        return Decimal(self.quantity) * self.product.price
