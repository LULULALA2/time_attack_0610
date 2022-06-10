from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "categories"
    name = models.CharField(max_length=20)


class Product(models.Model):
    class Meta:
        db_table = "products"

    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField()
    price = models.IntegerField(max_length=20)
    quantity = models.IntegerField(max_length=20)


class ProductOrder(models.Model):
    class Meta:
        db_table = "product_orders"

    user_order_quantity = models.IntegerField(max_length=20)


class OrderStatus(models.Model):
    class Meta:
        db_table = "order_status"

    order_status = models.CharField(max_length=20)


class UserOrder(models.Model):
    class Meta:
        db_table = "user_orders"

    shipping_address = models.TextField()
    order_time = models.DateTimeField(auto_now_add=True)
    total_product_price = models.CharField(max_length=20)
    discount_rate = models.FloatField(max_length=20)
    final_price = models.CharField(max_length=20)
    Validity = models.BooleanField(default=False)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    order_product_quantity = models.ForeignKey(ProductOrder, on_delete=models.CASCADE)

