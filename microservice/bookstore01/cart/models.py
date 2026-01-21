from django.db import models

class Cart(models.Model):
    customer = models.ForeignKey('users.Customer', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.customer.name}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey('catalog.Book', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def total_price(self):
        return self.book.price * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.book.title} in cart {self.cart.id}"