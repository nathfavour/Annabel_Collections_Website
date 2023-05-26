from django.contrib.auth.decorators import login_required
"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View
from django.db import transaction
from .models import Products, Cart
from .forms import BootstrapAuthenticationForm

from datetime import datetime
from django.http import HttpRequest


def Search(request):
    pass
    #q = request.GET.get('q', None)
    #items = ''
    #if q is None or q is "":
    #    products = Products.objects.all()
    #elif q is not None:
    #    product = Products.object.filter(title__contains = q)
    #return render (request, 'app/search.html', {'product' : product})

class RegisterPage(FormView):
    template_name = 'app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('products_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('products_list')
        return super(RegisterPage, self).get(*args, **kwargs)

def Developer(request):
    """Renders the developer info page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/developer.html',
        {
            'title':'Binary globe software services',
            'message':'contact us at tbinaryglobe@gmail.com for your software services like web design, app development and video editing',
            'year':datetime.now().year,
            'month': datetime.now().month,
        }
    )


def product_list(request):
    products = Products.object.all()

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Products.object.all(pk=product_id)
        product.ticked = not product.ticked
        product.save()
        return redirect('cart')

    return render(request, 'products/product_list.html', {'products' : products})
   
def cart(request):
    user = request.user
    cart, created = Cart.object.get_or_create(user=user)
    products = cart.products.all()

    return render(request, 'cart.html', {'products' : products})


#class Cart(LoginRequiredMixin, View):
#    model = Products
#    context_object_name = 'cart'
#    template_name = 'app/cart.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['cart'] = context['cart'].filter(user=self.request.user)
#        context['count'] = context['cart'].filter(Add = True).count()

#        search_input = self.request.GET.get('search-area') or ''
#        if search_input:
#            context['cart'] = context['cart'].filter(
#                title__contains=search_input)

#        context['search_input'] = search_input

#        return context


#class ProductListView(ListView):
#    model = Products
#    context_object_name = 'products'
#    template_name = "app/product_list.html"

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['product_list'] = context['product_list'].filter(user=self.request.user)
#        context['count'] = context['product_list'].filter(Available=True).count()

#        search_input = self.request.GET.get('search-area') or ''
#        if search_input:
#            context['product_list'] = context['product_list'].filter(
#                title__contains=search_input)

#        context['search_input'] = search_input

#        return context



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/home.html',
        {
            'title':'Home Page',
            'month':datetime.now().month,
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'You can contact us.',
            'year':datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About Annabel Anthony Collections',
            'message':'Annabel Anthony collections is a budding fashion industry that specialises in clothing, shoes and other exotic fashion accessories. Our services are pure gold and we do NOT dissapoint!',
            'year':datetime.now().year,
            'month': datetime.now().month,
        }
    )




