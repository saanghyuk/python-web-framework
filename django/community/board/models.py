from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='title')
    contents = models.TextField(verbose_name="contents")
    writer = models.ForeignKey(
        'fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='writer')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='Registered Time')

    def __str__(self):
        return self.title

    class Meta:
        # SQL에 들어갈 테이블 명 추가
        db_table = 'community_board'
        verbose_name = '커뮤니티 게시글'
        verbose_name_plural = '커뮤니티 게시글'
