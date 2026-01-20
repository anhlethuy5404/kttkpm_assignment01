from ..domain.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class CustomerUseCases:
    def register_customer(self, name, email, password, phone_number, dob):
        # Create user in auth_user table
        user = User.objects.create_user(username=email, email=email, password=password)
        
        # Create customer in Customer table
        customer = Customer.objects.create(
            name=name,
            email=email,
            password=user.password,  # Store the hashed password
            phoneNumber=phone_number,
            dob=dob
        )
        
        return customer

    def login_customer(self, request, email, password):
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return user
        return None
