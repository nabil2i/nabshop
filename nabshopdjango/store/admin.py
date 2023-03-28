from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils.html import format_html, urlencode

from . import models


# custom filter
class StockFilter(admin.SimpleListFilter):
  title = 'stock'
  parameter_name = 'stock'

  # define different settings
  def lookups(self, request, model_admin):
    return [
      ('<10', 'LOW')
    ]
  
  # implement the filtering logic here
  def queryset(self, request, queryset: QuerySet):
    if (self.value() == '<10'):
      return queryset.filter(stock__lt=10)


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
  list_display = ['title', 'books_count']
  search_fields = ['title']

  @admin.display(ordering="books_count")
  def books_count(self, genre):
    url = (
      reverse('admin:store_book_changelist')
            + '?'
            + urlencode({
                'genre__id': str(genre.id)
            }))
    return format_html('<a href="{}">{} Books</a>', url, genre.books_count)

  def get_queryset(self, request):
    return super().get_queryset(request).annotate(
      books_count=Count('books')
      )


class BookImageInline(admin.TabularInline):
  model = models.BookImage
  readonly_fields = ['thumbnail_image',
                     'get_image',
                     'get_thumbnail',
                     ]

  def thumbnail_image(self, instance):
    if instance.get_thumbnail() != '':
      return format_html(f'<img src="{instance.get_image()}" class="thumbnail"/>')
    return ''  
  

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
  """Customize the list page of books"""
  list_display = ['title', 'author', 'genre_title']
  list_select_related = ['genre']
  list_filter = ['genre', 'updated_at']
  search_fields = ['title', 'genre']
  inlines = [BookImageInline]

  def genre_title(self, book):
    return book.genre.title

  class Media:
    # load on bookadmin page
    css = {
      'all': ['store/styles.css']
    }


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ['first_name', 'last_name', 'country']


@admin.register(models.BookEdition)
class BookEditionAdmin(admin.ModelAdmin):
  prepopulated_fields = {
    'slug': ['isbn']  
  }
  autocomplete_fields = ['book']
  list_display = ['book_title', 'booktype', 'isbn', 'unit_price', 'publisher', 'stock_status']
  list_editable = ['unit_price']
  list_per_page = 10
  actions = ['clear_stock']
  list_filter = ['booktype', StockFilter]
  search_fields = ['book_title']
  
  # custom action
  @admin.action(description='Clear stock')
  def clear_stock(self, request, queryset):
    updated_count = queryset.update(stock=0)
    self.message_user(
      request,
      f'{updated_count} books were successfully updated.',
      messages.ERROR
    )

  def book_title(self, bookedition):
    return bookedition.book.title

  @admin.display(ordering='stock')
  def stock_status(self, bookedition):
    if bookedition.stock < 10:
      return 'Low'
    return 'OK'


@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
  list_display = ['publisherhouse', 'country', 'city']


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
  list_display = ['first_name', 'last_name', 'orders']
  list_per_page = 10
  list_select_related = ['user']
  ordering = ['user__first_name', 'user__last_name']
  search_fields = ['first_name__istartswith', 'last_name__istartswith']
  autocomplete_fields = ['user']

  @admin.display(ordering='orders_count')
  def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': str(customer.id)
            }))
        return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count)

  def get_queryset(self, request):
    return super().get_queryset(request).annotate(
      orders_count=Count('orders'))


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['bookedition']
    min_num = 1
    max_num = 10
    model = models.OrderItem
    extra = 0

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
  list_display = ['id', 'placed_at', 'total_amount',
                  'payment_status', 'delivery_status', 'customer',
                  'phone']
  list_per_page = 10
  list_select_related = ['customer']
  autocomplete_fields = ['customer']
  inlines = [OrderItemInline]
