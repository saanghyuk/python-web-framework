# Django Function



- **Many To Many** 

  어느 모델에 정의해도 상관 없음. 주된 모델에 정의하면 Ok

  ```python
  class Board(models.Model):
      
      # 1:N Relationship
      writer = models.ForeignKey(
          'fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='writer')
  		# N:M Relationship
      tags = models.ManyToManyField('tag.Tag', verbose_name='#Tag')
  
  
  ```

  

- **Get Or Create**

  해당 조건이 일치하면, 가지고 오고 아니면, 생성. 

  앞에서는 생성 혹은 기존 객체, 두번째는 생성됬는지 여부 Boolean

  ```python
  
              for tag in tags:
                  if not tag:
                      continue
                  # IMPORTANT
                  _tag, created = Tag.objects.get_or_create(name=tag)
                  board.tags.add(_tag)
  
  ```











