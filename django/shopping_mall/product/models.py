from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name="PRODUCT NAME")
    price = models.IntegerField(verbose_name="PRODUCT PRICE")
    description = models.TextField(verbose_name="PRODUCT DESCRIPTION")
    stock = models.IntegerField(verbose_name="STOCK")
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name="REGI DATE")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Shopping_Product"
        verbose_name = "Product"
        verbose_name_plural = "Product"
