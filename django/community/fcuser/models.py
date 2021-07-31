from django.db import models

# Create your models here.


class Fcuser(models.Model):
    username = models.CharField(max_length=64, verbose_name='User Name')
    useremail = models.EmailField(max_length=128, verbose_name="User Email")
    password = models.CharField(max_length=64, verbose_name='Password')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='Registered Time')

    def __str__(self):
        return self.username

    class Meta:
        # SQL에 들어갈 테이블 명 추가
        db_table = 'community_fcuser'
        verbose_name = 'Fcuser 사용자'
        verbose_name_plural = 'Fcuser 사용자'
