from django.shortcuts import render
from .models import Book
from bookstore01.users.models import Customer

def home(request):
    books = Book.objects.all()
    customer = None
    if request.user.is_authenticated:
        try:
            customer = Customer.objects.get(email=request.user.email)
        except Customer.DoesNotExist:
            pass
    return render(request, 'home.html', {'books': books, 'customer': customer})