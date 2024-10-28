from django.contrib import admin

from .models import BookInstance, Book, Genre, Author

admin.site.register(BookInstance)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)