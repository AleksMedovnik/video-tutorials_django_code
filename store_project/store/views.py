from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.views.generic import ListView, DetailView


class HomeView(ListView):
    model = Product


def product_list(request):
    categories = Category.objects.all()
    search_query = request.GET.get('search', None)
    if search_query:
        product_list = Product.objects.filter(
            Q(title__icontains=search_query)
            |
            Q(info__icontains=search_query)
        )
    else:
        product_list = Product.objects.all()
    return render(
        request,
        'store/product_list.html',
        context={
            'product_list': product_list,
            'categories': categories
        }
    )


class ProductView(DetailView):
    model = Product


def product_detail(request, pk):
    categories = Category.objects.all()
    product = Product.objects.get(pk=pk)
    return render(
        request,
        'store/product_detail.html',
        context={'product': product, 'categories': categories}
    )


def category_detail(request, pk):
    categories = Category.objects.all()
    category = Category.objects.get(pk=pk)
    product_list = category.products.all()
    return render(
        request,
        'store/category_detail.html',
        context={
            'product_list': product_list,
            'category': category,
            'categories': categories
        }
    )


def save_order(request):
    categories = Category.objects.all()
    order = Order()
    order.name = request.POST['user_name']
    order.email = request.POST['user_email']
    order.product = Product.objects.get(pk=request.POST['product_id'])
    order.save()
    return render(
        request,
        'store/order.html',
        context={
            'categories': categories,
            'order': order
        }
    )