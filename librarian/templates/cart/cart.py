from django.conf import settings
from librarian.models import Book
from decimal import Decimal


class Cart(object):

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
