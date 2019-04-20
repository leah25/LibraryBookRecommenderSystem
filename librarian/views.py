from django.shortcuts import render, get_object_or_404
from .models import Category, Book
from cart.forms import CartAddBookForm
from .models import Actor
from django import forms


def book_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    books = Book.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = Book.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'books': books
    }
    return render(request, 'librarian/book/list.html', context)


def book_detail(request, id, slug):
    book = get_object_or_404(Book, id=id, slug=slug, available=True)
    cart_book_form = CartAddBookForm()
    context = {
        'book': book,
        'cart_book_form': cart_book_form
    }
    return render(request, 'librarian/book/detail.html', context)

class ActorSearchForm(forms.Form):
    search_text =  forms.CharField(
        required = False,
        label='Search name or surname!',
        widget=forms.TextInput(attrs={'placeholder': 'search here!'})
    )

    search_age_exact = forms.IntegerField(
        required = False,
        label='Search age (exact match)!'
    )

    search_age_min = forms.IntegerField(
        required = False,
        label='Min age'
    )

    search_age_max = forms.IntegerField(
      required = False,
      label='Max age'
    )
