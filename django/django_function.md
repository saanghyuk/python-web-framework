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

  ```python
  # 사진 같은거 나오게 해줌. 
  <li class="list-group-item">Description : {{ product.description|safe }}</li>
  ```

  





- Class 기반의 뷰에서 폼을 같이 넘길 때, 

  ```python
  class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'
  
    # 원하는 정보 같이 넣어서 전달하게 해주는 함수 제공.
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form'] = OrderForm
      return context
  ```

  

- Form의 clean에서 여러가지 모델에 관한 처리 하는데, 이때 request.session을 못쓰는게 항상 문제임. 

  **form에다가 리퀘스트를 같이 싣어 주는 코드.** 

  지금 구조가, product_detail이라는 Html을 Product에 있는 view에서 만들면서, 그 안에 들어가는 폼뷰를 같이 쏴주는 형태. `get_context_data` 이걸로. 

  일단 form 자체에서 __init__할때 리퀘스트 받아서 스스로 인스턴스에 저장할 수 있도록 생성자 함수 수정해주고, 

  ```python
  forms.py
  # 생성자 수정해서, 폼이 만들어 지면서, request인자 받으면서 생성되도록 
  
  class OrderForm(forms.Form):
      def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
  
      quantity = forms.IntegerField(error_messages={
          'required': "Please Select the Quantity"
      }, label="quantity")
  
      product = forms.IntegerField(
        label = "product", widget  = forms.HiddenInput
      )
  ```

  그리고, 이 폼 만들어 주는 곳에서 Init을 하기로 했으면, 실제로 만드는 곳에서 이걸 넣어 줘야지. 

  ```Python
  # 폼이 만들어 지면서, 리퀘스트 정보를 넣어서 그 채로 템플릿으로 보내준다. 
  
  class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'
  
    # 원하는 정보 같이 넣어서 전달하게 해주는 함수 제공.
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form'] = OrderForm(self.request)
      return context
  ```

  근데 지금 이 폼의 POST는 또, /order/create가 라는 다른 url에서 받고 있는데, 

  얘는 order앱의 view에서 정의되 있음 여기서도, 수정 해야함. 거기까지도 수정해 줘야 함. 

  ```python
  # 받는 쪽에서도, 받은 다음에 다시 form으로 보내서 거기서 검증을 하는데, 
  # 그때 다시 form이 받을 수 있도록, kw에 싣어서 보내주는 것. 
  
  class OrderCreate(FormView):
      form_class = OrderForm
      success_url = '/product/'
  
      def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
          'request' : self.request
        })
        return kw
  ```

  