from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView
from .models import Product
from .forms import RegisterForm
from order.forms import OrderForm
# Create your views here.

class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'


class ProductList(ListView):
  model = Product
  template_name="product.html"
  # context_object_name 설정 안하면, object_list로 넘어감
  context_object_name = 'product_list'


class ProductDetail(DetailView):
  template_name = 'product_detail.html'
  queryset = Product.objects.all()
  context_object_name = 'product'

  # 원하는 정보 같이 넣어서 전달하게 해주는 함수 제공.
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['form'] = OrderForm(self.request)
    return context