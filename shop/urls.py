from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<int:category_id>/', views.product_list, name='product_list_by_category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('remove_cart/<int:item_id>/', views.remove_cart, name='remove_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='order_history'),
]