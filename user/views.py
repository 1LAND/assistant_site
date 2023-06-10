from django.shortcuts import render,redirect
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from .forms import RegisterUserForm,LoginUserForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import RegisterUserForm,LoginUserForm
from django.contrib.auth.models import User
# Create your views here.

class RegisterUser(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
def account(request):
    if request.user.is_authenticated:
        return render(request, 'user/account.html')
    else:
        return redirect('login')