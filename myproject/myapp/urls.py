from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('books/create/', views.create_book_view, name='create_book'),
]
