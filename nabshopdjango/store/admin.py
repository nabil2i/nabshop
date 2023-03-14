from django.contrib import admin

from . import models


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
  list_display = ['title']

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
  """Customize the list page of books"""
  list_display = ['title', 'author', 'genre']

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ['first_name', 'last_name', 'country']

@admin.register(models.BookEdition)
class BookEditionAdmin(admin.ModelAdmin):
  list_display = ['book', 'booktype', 'isbn', 'unit_price', 'publisher']
  list_editable = ['unit_price']
  list_per_page = 10

@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
  list_display = ['publisherhouse', 'country', 'city']



