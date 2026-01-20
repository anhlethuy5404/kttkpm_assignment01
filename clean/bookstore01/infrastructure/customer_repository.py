from ..domain.models import Customer
from django.contrib.auth.hashers import make_password, check_password

class CustomerRepository:
    def create_customer(self, name, email, password, phone_number, dob):
        hashed_password = make_password(password)
        customer = Customer(
            name=name,
            email=email,
            password=hashed_password,
            phoneNumber=phone_number,
            dob=dob
        )
        customer.save()
        return customer

    def get_customer_by_email(self, email):
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return None

    def verify_password(self, customer, password):
        return check_password(password, customer.password)
