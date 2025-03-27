from django import forms
from .models import Book

# Creating Basic (FORM)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

# Creating MODEL (FORM)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'price', 'genres']
        # You can also use exclude to specify fields to exclude:
        # exclude = ['some_field']
        widget = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
            'genres': forms.CheckboxSelectMultiple,
        }
        labels = {
            'title': 'Book Title',
            'publication_date': 'Release Date',
        }
        help_texts = {
            'price': 'Enter the price in USD.',
        }
