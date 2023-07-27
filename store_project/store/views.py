from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .utils import CategoriesMixin
from django.http import HttpResponse


def work(request):
    # p = Product(title='Ford', price=20000)
    # p.save()

    # Product.objects.create(title='BMW', price=25000)

    # obj = Product.objects.get(pk=10)
    # obj.price += 5000

    # Product.objects.filter(pk=10).update(price=30000)

    # obj = Product.objects.get(pk=10).delete()

    # obj = Product.objects.exclude(title='Ford')

    # obj = Product.objects.all().order_by('-pk')

    # obj = Product.objects.filter(title='Ford').count()

    # obj = Product.objects.filter(title='Lada').exists()

    # obj = Product.objects.filter(price__gt=100000) # >
    # obj = Product.objects.filter(price__gte=100000) # >=
    # obj = Product.objects.filter(price__lt=100000) # <
    # obj = Product.objects.filter(price__lte=100000)  # <=
    # obj = Product.objects.filter(price__in=(25000, 20000, 100000)) 

    # obj = Product.objects.filter(title__exact='range RoveR Sport') 
    # obj = Product.objects.filter(title__iexact='range RoveR Sport') 

    # obj = Product.objects.filter(title__contains='Rover') 
    # obj = Product.objects.filter(title__icontains='rovER') 

    # o = Order.objects.select_related('product').get(pk=1)
    # p = o.product

    # p = Product.objects.prefetch_related('categories').get(pk=1)
    # cats = p.categories.all()
    
    return HttpResponse('Hello')


class HomeView(ListView, CategoriesMixin):
    model = Product

    def get_queryset(self):
        search_query = self.request.GET.get('search', None)
        if search_query:
            return self.model.objects.filter(
                Q(title__icontains=search_query)
                |
                Q(info__icontains=search_query)
            )
        return Product.objects.all()


class ProductView(DetailView, CategoriesMixin):
    model = Product


class CategoryView(DetailView, CategoriesMixin):
    model = Category


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