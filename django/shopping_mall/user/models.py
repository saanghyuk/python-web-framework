from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(verbose_name="EMAIL")
    password = models.CharField(max_length=128, verbose_name="PASSWORD")
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name="REGI DATE")
    level = models.CharField(max_length=8, verbose_name="USER LEVEL", default="user",
            choices = (
                ('admin', 'admin'),
                ('user', 'user')
            )
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = "Shopping_User"
        verbose_name = "User"
        verbose_name_plural = "User"
