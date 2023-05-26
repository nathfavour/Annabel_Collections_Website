"""
Definition of urls for Django_test_1.

"""

from datetime import datetime
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from app import forms, views
from .views import RegisterPage

urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year
             }
         ),
         name='login'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('developer/', views.Developer, name = 'developer'),
    path('', views.home, name='home'),
    path('search/', views.Search, name = 'search'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('cart/', views.cart, name = 'cart'),
    path('products/', views.product_list, name = 'product_list')

]
