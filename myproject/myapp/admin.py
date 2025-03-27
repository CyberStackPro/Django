from django.contrib import admin
from .models import Author, Genre, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',
                    'publication_date', 'price', 'description')
    list_filter = ('author', 'genres', 'publication_date')
    search_fields = ('title', 'author__name')
    # ordering = ('-publication_date',)
    ordering = ('title',)
    fieldsets = [
        ('Book Information', {'fields': [
         'title', 'author', 'publication_date']}),
        ('Pricing', {'fields': ['price']}),
        ('Categorization', {'fields': ['genres']}),
    ]
    readonly_fields = ('publication_date',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name',)
    ordering = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
