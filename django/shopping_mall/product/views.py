from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView
from .models import Product
from .forms import RegisterForm
from order.forms import OrderForm
from django.utils.decorators import method_decorator
from user.decorator import login_required, admin_required
from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer
# Create your views here.


class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')
    # RetrieveMixin은 자동으로 url의 pk가져옴.

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            description=form.data.get('description'),
            stock=form.data.get('stock'),
        )
        product.save()
        return super().form_valid(form)


class ProductList(ListView):
    model = Product
    template_name = "product.html"
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
