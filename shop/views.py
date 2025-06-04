from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required
from accounts.models import CustomerProfile
from django.contrib import messages

def product_list(request, category_id=None):
    categories = Category.objects.all()
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity', 1))
        except (TypeError, ValueError):
            quantity = 1
    else:
        quantity = 1
    quantity = max(1, min(quantity, product.stock))  # Ensure within stock limits

    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    # Do not exceed stock
    cart_item.quantity = min(cart_item.quantity, product.stock)
    cart_item.save()
    messages.success(request, 'Product added to cart!')
    return redirect('cart')

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def remove_cart(request, item_id):
    CartItem.objects.get(pk=item_id, user=request.user).delete()
    return redirect('cart')

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        messages.warning(request, 'Your cart is empty.')
        return redirect('cart')
    profile = CustomerProfile.objects.get(user=request.user)
    if request.method == 'POST':
        address = request.POST.get('address')
        order = Order.objects.create(
            user=request.user,
            delivery_address=address,
            is_cod=True,
            status='Pending'
        )
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )
            # Reduce stock
            item.product.stock -= item.quantity
            item.product.save()
        cart_items.delete()
        messages.success(request, 'Order placed successfully!')
        return redirect('order_history')
    return render(request, 'shop/checkout.html', {'profile': profile, 'cart_items': cart_items})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-ordered_at')
    return render(request, 'shop/order_history.html', {'orders': orders})