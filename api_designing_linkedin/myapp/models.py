from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=32)
    brand = models.CharField(max_length=32)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    address = models.TextField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return f"{self.first_name} -- {self.id}"

class OrderProduct(models.Model):
    product = models.ForeignKey(Product, related_name="product_orders", on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, related_name="order_products", on_delete=models.CASCADE)

