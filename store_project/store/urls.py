from django.urls import path
from .views import HomeView, ProductView, product_list, product_detail, category_detail, save_order

urlpatterns = [
    path('', HomeView.as_view(), name='product_list_url'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_detail_url'),
    path('category/<int:pk>/', category_detail, name='category_detail_url'),
    path('save_order', save_order),
]
