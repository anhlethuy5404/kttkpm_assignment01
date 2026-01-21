from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from bookstore01.users.models import Customer
from bookstore01.catalog.models import Book

@login_required
def add_to_cart(request, book_id):
    if request.method == 'POST':
        try:
            customer = Customer.objects.get(email=request.user.email)
            book = get_object_or_404(Book, id=book_id)
            quantity = int(request.POST.get('quantity', 1))

            cart, _ = Cart.objects.get_or_create(customer=customer)
            
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart, 
                book=book,
                defaults={'quantity': quantity}
            )
            
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            
            messages.success(request, 'Book added to cart.')
        except Customer.DoesNotExist:
            messages.error(request, 'Customer profile not found.')
        
        return redirect('home')
    return redirect('home')

@login_required
def view_cart(request):
    try:
        customer = Customer.objects.get(email=request.user.email)
        cart = Cart.objects.filter(customer=customer).first()
        cart_items = CartItem.objects.filter(cart=cart) if cart else []
        total_price = sum(item.total_price for item in cart_items)
            
        return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'customer': customer})
    except Customer.DoesNotExist:
        messages.error(request, 'Customer profile not found.')
        return redirect('home')