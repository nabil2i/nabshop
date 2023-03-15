from decimal import Decimal

from django.conf import settings
from django.db import transaction
from rest_framework import serializers

from .models import (Address, Author, Book, BookEdition, BookImage, Cart,
                     CartItem, Customer, Genre, Order, OrderItem, Publisher,
                     Review)


class GenreSerializer(serializers.ModelSerializer):
  """Serializer for Genre model"""
  class Meta:
    model = Genre
    fields = ['id', 'title', 'books_count']

  books_count = serializers.IntegerField(read_only=True)


class SimpleGenreSerializer(serializers.ModelSerializer):
  """Serializer for simple Genre model"""
  class Meta:
    model = Genre
    fields = ['id', 'title']


class AuthorSerializer(serializers.ModelSerializer):
  """Serializer for Author model"""
  class Meta:
    model = Author
    fields = ['id', 'first_name', 'last_name']

class PublisherSerializer(serializers.ModelSerializer):
  """Serializer for simple Genre model"""
  class Meta:
    model = Publisher
    fields = ['id', 'publisherhouse', 'city', 'country']


class SimpleBookSerializer(serializers.ModelSerializer):
  """Serializer for displaying a Book in BookEdition"""
  author = AuthorSerializer(read_only=True)
  genre = SimpleGenreSerializer(read_only=True)

  class Meta:
    model = Book
    fields = ['id', 'title', 'author', 'genre']


class SimplestBookSerializer(serializers.ModelSerializer):
  """Serializer for the simplest Book"""

  class Meta:
    model = Book
    fields = ['id', 'title']


class BookEditionSerializer(serializers.ModelSerializer):
  """Serializer for BookEdition model"""
  book = SimpleBookSerializer(read_only=True)
  publisher = PublisherSerializer(read_only=True)

  class Meta:
    model = BookEdition
    fields = ['id', 'book', 'booktype', 'isbn', 'unit_price',
              'price_with_tax', 'pages', 'bookformat',
              'publisher', 'publicationdate', 'stock']

  price_with_tax = serializers.SerializerMethodField(
    method_name='calculate_tax'
  )

  def calculate_tax(self, bookedition: BookEdition):
    return bookedition.unit_price * Decimal(1)


class SimpleBookEditionSerializer(serializers.ModelSerializer):
  """Serializer for simple BookEdition model"""
  # publisher = PublisherSerializer(read_only=True)
  publisher = serializers.StringRelatedField()

  class Meta:
    model = BookEdition
    fields = ['id', 'booktype', 'isbn', 'unit_price',
              'price_with_tax', 'stock',
              'pages', 'bookformat', 'publisher',
              'publicationdate']
  
  price_with_tax = serializers.SerializerMethodField(
    method_name='calculate_tax'
  )

  def calculate_tax(self, bookedition: BookEdition):
    return bookedition.unit_price * Decimal(1)

class SimplestBookEditionSerializer(serializers.ModelSerializer):
  """Serializer for simplest BookEdition model"""
  # book = SimplestBookSerializer()
  book = serializers.StringRelatedField()
  # book__title = serializers.StringRelatedField(read_only=True)
  
  class Meta:
    model = BookEdition
    fields = ['id', 'book', 'booktype', 'unit_price']


class BookImageSerializer(serializers.ModelSerializer):
  """Serializer for BookImage"""
  # def create(self, validated_data):
  #   book_id = self.context['book_id']
  #   return BookImage.objects.create(book_id=book_id, **validated_data)

  class Meta:
    model = BookImage
    fields = ['id', 'get_image', 'get_thumbnail']


class BookSerializer(serializers.ModelSerializer):
  """Serializer for Book model"""
  bookeditions = SimpleBookEditionSerializer(many=True, read_only=True)
  images = BookImageSerializer(many=True, read_only=True)
  # author = AuthorSerializer()
  author = serializers.StringRelatedField()
  # genre = SimpleGenreSerializer()
  genre = serializers.StringRelatedField()

  class Meta:
    model = Book
    fields = ['id',
              'title',
              'description',
              'slug',
              'author',
              'genre',
              'bookeditions',
              'images'
    ]


# class SimpleUserSerializer(serializers.ModelSerializer):
#   """Seralizer for a User displayed in the review"""
#   class Meta:
#     model = settings.AUTH_USER_MODEL
#     fields = ['id', 'first_name', 'last_name']


# class CustomerReviewSerializer(serializers.ModelSerializer):
#   """Serializer for a Customer of a Review"""
#   user = SimpleUserSerializer(read_only=True)

#   class Meta:
#     model = Customer
#     fields = ['id', 'user']


class ReviewSerializer(serializers.ModelSerializer):
  """Serializer for Review model"""
  customer = serializers.StringRelatedField()
  # customer_id = serializers.IntegerField(read_only=True)

  class Meta:
    model = Review
    fields = ['id', 'created_at',
              'customer', 'description'
    ]

  def create(self, validated_data):
    book_id = self.context['book_id']
    customer_id = self.context['customer_id']
    return Review.objects.create(book_id=book_id,
                                 customer_id=customer_id,
                                 **validated_data)


class CartItemSerializer(serializers.ModelSerializer):
  """Serializer for CartItem model"""
  bookedition = SimplestBookEditionSerializer()
  # bookedition = serializers.StringRelatedField()
  total_price = serializers.SerializerMethodField()

  def get_total_price(self, cart_item: CartItem):
    return cart_item.quantity * cart_item.bookedition.unit_price

  class Meta:
    model = CartItem
    fields = ['id', 'bookedition', 'quantity', 'total_price']


class CartSerializer(serializers.ModelSerializer):
  """Serializer for Cart model"""
  id = serializers.UUIDField(read_only=True)
  items = CartItemSerializer(many=True, read_only=True)
  total_price = serializers.SerializerMethodField()

  def get_total_price(self, cart):
    return sum([item.quantity * item.bookedition.unit_price  for item in cart.items.all()])

  class Meta:
    model = Cart
    fields = ['id', 'items', 'total_price']


class AddCartItemSerializer(serializers.ModelSerializer):
  """Serializer to add a cart item"""
  bookedition_id = serializers.IntegerField()

  def validate_bookedition_id(self, value):
    if not BookEdition.objects.filter(pk=value).exists():
      raise serializers.ValidationError(
        'The book with the given ID is not found'
      )
    return value

  def save(self, **kwargs):
    cart_id = self.context['cart_id']
    bookedition_id = self.validated_data['bookedition_id']
    quantity = self.validated_data['quantity']

    try:
      cart_item = CartItem.objects.get(
        cart_id=cart_id, bookedition_id=bookedition_id)
      cart_item.quantity += quantity
      cart_item.save()
      self.instance = cart_item
    except CartItem.DoesNotExist:
      # create new item
      self.instance = CartItem.objects.create(
        cart_id=cart_id, **self.validated_data
      )

    return self.instance

  class Meta:
    model = CartItem
    fields = ['id', 'bookedition_id', 'quantity']


# class RemoveCartItemSerializer(serializers.ModelSerializer):
#   """Serializer to add a cart item"""
#   bookedition_id = serializers.IntegerField()

#   def validate_bookedition_id(self, value):
#     if not BookEdition.objects.filter(pk=value).exists():
#       raise serializers.ValidationError(
#         'The book with the given ID is not found'
#       )
#     return value

#   def save(self, **kwargs):
#     cart_id = self.context['cart_id']
#     bookedition_id = self.validated_data['bookedition_id']
#     quantity = self.validated_data['quantity']

#     try:
#       cart_item = CartItem.objects.get(
#         cart_id=cart_id, bookedition_id=bookedition_id)
#       cart_item.quantity += quantity
#       cart_item.save()
#       self.instance = cart_item
#     except CartItem.DoesNotExist:
#       self.instance = CartItem.objects.create(
#         cart_id=cart_id, **self.validated_data
#       )

#     return self.instance

#   class Meta:
#     model = CartItem
#     fields = ['id', 'bookedition_id', 'quantity']


class UpdateCartItemSerializer(serializers.ModelSerializer):
  """Update a CartItem"""
  class Meta:
    model = CartItem
    fields = ['quantity']

class CustomerSerializer(serializers.ModelSerializer):
  """Serializer for a Customer"""
  user_id = serializers.IntegerField(read_only=True)

  class Meta:
    model = Customer
    fields = ['id', 'user_id', 'phone', 'birth_date']


class OrderItemSerializer(serializers.ModelSerializer):
  """Serializer for OrderItem"""
  bookedition = SimplestBookEditionSerializer()

  class Meta:
    model = OrderItem
    fields = ['id', 'bookedition', 'unit_price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for an Order"""
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'placed_at', 'payment_status', 'items']


class UpdateOrderSerializer(serializers.ModelSerializer):
  """Serializer for updating an Order"""
  class Meta:
    model = Order
    fields = ['payment_status']


class CreateOrderSerializer(serializers.Serializer):
  """Serializer for creating an order"""
  cart_id = serializers.UUIDField()

  def validate_cart_id(self, cart_id):
    if not Cart.objects.filter(pk=cart_id).exists():
      raise serializers.ValidationError(
        'There is no cart with the given ID'
      )
    if CartItem.objects.filter(cart_id=cart_id).count() == 0:
      raise serializers.ValidationError('The cart is empty!')
    return cart_id

  def save(self, **kwargs):
    with transaction.atomic():
      # retrive the cart_id
      cart_id = self.validated_data['cart_id']

      # retrive the customer to place the order
      customer = Customer.objects.get(
        user_id=self.context['user_id']
      )
      # create the order
      order = Order.objects.create(customer=customer)

      # retrieve the items in the cart
      cart_items = CartItem.objects \
        .select_related('bookedition') \
        .filter(cart_id=cart_id)
      # move the cart  items into the order
      order_items = [
        OrderItem(
          order=order,
          bookedition=item.bookedition,
          unit_price=item.bookedition.unit_price,
          quantity=item.quantity
        ) for item in cart_items
      ]
      # we bulk create the order items for performance
      OrderItem.objects.bulk_create(order_items)

      # delete the cart
      Cart.objects.filter(pk=cart_id).delete()

      order_created.send_robust(self.__class__, order=order)

      return order
