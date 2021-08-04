from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import Product
from .forms import RegisterForm
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


