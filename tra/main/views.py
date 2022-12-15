from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView

from .models import Product, Category


# Create your views here.

def index(request):
    num_product = Product.objects.filter()[:4]
    return render(request, 'index.html', context={'num_product': num_product})


class ProductView(ListView):
    model = Product


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


class Login(LoginView):
    template_name = 'login.html'


class Logout(LogoutView):
    template_name = 'login.html'


class RegistrationUser(CreateView):
    model = User
    template_name = 'registration.html'
    fields = ['username', 'email', 'password']
    success_url = reverse_lazy('index')


class CreateProductView(CreateView):
    model = Product
    template_name = 'create_product.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


class CreateCategoryView(CreateView):
    model = Category
    template_name = 'create_categori.html'
    fields = '__all__'
    success_url = reverse_lazy('index')
