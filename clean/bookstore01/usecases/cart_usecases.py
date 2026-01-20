from ..domain.models import Cart, CartItem, Book, Customer

class CartUseCases:
    def add_to_cart(self, customer_id, book_id, quantity):
        try:
            customer = Customer.objects.get(id=customer_id)
            book = Book.objects.get(id=book_id)
            
            cart, created = Cart.objects.get_or_create(customer=customer)
            
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart, 
                book=book,
                defaults={'quantity': quantity}
            )
            
            if not created:
                cart_item.quantity += quantity
            
            cart_item.save()
            
            return cart_item
        except (Customer.DoesNotExist, Book.DoesNotExist):
            return None

    def get_cart_items(self, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            cart = Cart.objects.get(customer=customer)
            cart_items = CartItem.objects.filter(cart=cart)
            return cart_items
        except (Customer.DoesNotExist, Cart.DoesNotExist):
            return None
