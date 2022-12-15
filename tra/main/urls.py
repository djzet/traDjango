from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.ProductView.as_view(), name='product'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('accounts/', views.RegistrationUser.as_view(), name='registration'),
    path('createpro/', views.CreateProductView.as_view(), name='createpro'),
    path('createcat/', views.CreateCategoryView.as_view(), name='createcat'),
]