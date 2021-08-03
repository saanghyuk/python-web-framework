from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="Tag Name")
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='Registered Time')

    def __str__(self):
        return self.name

    class Meta:
        # SQL에 들어갈 테이블 명 추가
        db_table = 'community_tag'
        verbose_name = 'BOARD TAG'
        verbose_name_plural = 'BOARD TAG'
