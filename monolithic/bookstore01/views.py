from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Book, Customer, Cart, CartItem

class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        dob = request.POST.get('dob')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'registration/register.html')

        try:
            # Create Auth User
            user = User.objects.create_user(username=email, email=email, password=password)
            
            # Create Customer Profile
            Customer.objects.create(
                name=name,
                email=email,
                password=user.password,
                phoneNumber=phone_number,
                dob=dob
            )
            
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Registration failed: {e}')
            return render(request, 'registration/register.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
            return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
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