from django.shortcuts import render, redirect
from django.views import View
from ..usecases.customer_usecases import CustomerUseCases
from django.contrib import messages
from ..domain.models import Book, Customer
from ..usecases.cart_usecases import CartUseCases

class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        dob = request.POST.get('dob')

        customer_usecases = CustomerUseCases()
        customer = customer_usecases.register_customer(name, email, password, phone_number, dob)

        if customer:
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please try again.')
            return render(request, 'registration/register.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer_usecases = CustomerUseCases()
        user = customer_usecases.login_customer(request, email, password)

        if user:
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return render(request, 'registration/login.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')

def add_to_cart(request, book_id):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        
        try:
            customer = Customer.objects.get(email=request.user.email)
            quantity = int(request.POST.get('quantity', 1))
            
            cart_usecases = CartUseCases()
            cart_usecases.add_to_cart(customer.id, book_id, quantity)
            
            messages.success(request, 'Book added to cart.')
        except Customer.DoesNotExist:
            messages.error(request, 'Customer profile not found.')
        
        return redirect('home')

def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    try:
        customer = Customer.objects.get(email=request.user.email)
        cart_usecases = CartUseCases()
        cart_items = cart_usecases.get_cart_items(customer.id)
        
        total_price = sum(item.book.price * item.quantity for item in cart_items) if cart_items else 0
        
        return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'customer': customer})
    except Customer.DoesNotExist:
        messages.error(request, 'Customer profile not found.')
        return redirect('home')

def home(request):
    books = Book.objects.all()
    customer = None
    if request.user.is_authenticated:
        try:
            customer = Customer.objects.get(email=request.user.email)
        except Customer.DoesNotExist:
            pass
    return render(request, 'home.html', {'books': books, 'customer': customer})
