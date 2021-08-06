from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm
from django.contrib.auth.hashers import make_password
from user.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html', {"email": request.session.get('user')})

def logout(request):
    if 'user' in request.session:
        del(request.session['user'])
    return redirect('/')

# Form View
# This class is directly connected to urls.py
class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        print(form)
        user = User(
                        email=form.data.get('email'),
                        password=make_password(form.data.get('password'),)
                    )
        user.save()
        return super().form_valid(form)



class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    # 유효성 검사 끝나고 실행되는 함수
    def form_valid(self, form):
        # forms에서 성공시 싣어 보내 줬음.
        # self.request.session['user'] = form.email
        self.request.session['user'] = form.data.get('email')
        return super().form_valid(form)