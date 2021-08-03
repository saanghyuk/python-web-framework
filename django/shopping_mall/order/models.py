from django.db import models

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name="USER")
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, verbose_name="PRODUCT")
    quantity = models.IntegerField(verbose_name="QUANTITY")
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name="REGI DATE")

    def __str__(self):
        return str(self.user) + ' ' + str(self.product)

    class Meta:
        db_table = "Shopping_Order"
        verbose_name = "Order"
        verbose_name_plural = "Order"
