from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import OrderForm


# Create your views here.

class OrderCreate(FormView):
    form_class = OrderForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/'+str(form.product))

        # return redirect(self.request, 'product_detail.html', {"form":form})

    def get_form_kwargs(self, **kwargs):
      kw = super().get_form_kwargs(**kwargs)

      kw.update({
        'request' : self.request
      })
      return kw



    # # 유효성 검사 끝나고 실행되는 함수
    # def form_valid(self, form):
    #     # forms에서 성공시 싣어 보내 줬음.
    #     print(form.product)
    #     print(form.quantity)
    #     print(self.request.session['user'])
    #     # self.request.session['user'] = form.email
    #     return super().form_valid(form)fjfkdkkd
