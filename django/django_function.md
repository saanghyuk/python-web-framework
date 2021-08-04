# Django Function



[Class View](###ClassView)



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







- ### ClassView

  장고 안에 기본적으로 만들어져있는 뷰들이 있다. 

  [Class View Options](https://docs.djangoproject.com/en/3.2/topics/class-based-views/)

  어떻게 보여줄지만, html코드로 작성하면 된다. 

  



- ### Humanize

  [django template builtin filter](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/)

  html템플릿에서 여러 필터 사용할 수 있게 해줌. 예를 들어, 가격 3자리마다, 를 찍던가 날짜 형식을 바꾸던가. 

  Settings에 등록하고 상단에 Load해야 사용 가능. 

  *settings.py*

  ```python
  
  INSTALLED_APPS = [
  		...
      'django.contrib.humanize',
      ...
  ]
  
  ```

  HTML상단에 

  `{% load humanize %}`

  예시: 

  ```python
  <th scope="row">{{ product.price|intcomma }} Won</th>
  <th scope="row">{{ product.register_date|date:'Y-m-d H:i' }}</th>
  ```

  

