from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import ContactForm, BookForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact_view(request):
    # return render(request, 'contact.html', {'form': form})
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            return redirect('contact_success')
        else:
            form = ContactForm()
            return render(request, 'contact.html', {'form': form})


def create_book_view(request):
    # form = BookForm()
    # return render(request, 'create_book.html', {'form': form})
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm()
        return render(request, 'create_book.html', {'form': form})


def contact_success(request):
    return render(request, 'contact_success.html')


def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_detail.html', {'book': book})
