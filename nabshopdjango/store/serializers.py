from decimal import Decimal

from django.conf import settings
from django.db import transaction
from rest_framework import serializers

from .models import (Address, Author, Book, BookEdition, BookImage, Cart,
                     CartItem, Customer, Genre, Order, OrderItem, Publisher,
                     Review)
from .signals import order_created
import stripe

class GenreSerializer(serializers.ModelSerializer):
  """Serializer for Genre model"""
  class Meta:
    model = Genre
    fields = ['id', 'title', 'books_count', 'get_id_url']

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


class BookImageSerializer(serializers.ModelSerializer):
  """Serializer for BookImage"""
  def create(self, validated_data):
    book_id = self.context['book_id']
    return BookImage.objects.create(book_id=book_id, **validated_data)

  class Meta:
    model = BookImage
    fields = ['id', 'image', 'get_image', 'get_thumbnail']


class SimpleBookSerializer(serializers.ModelSerializer):
  """Serializer for displaying a Book in BookEdition"""
  author = AuthorSerializer(read_only=True)
  genre = SimpleGenreSerializer(read_only=True)

  class Meta:
    model = Book
    fields = ['id', 'title', 'author', 'genre']

class MyBookSerializer(serializers.ModelSerializer):
  """Serializer for displaying a Book in BookEdition"""
  # author = AuthorSerializer(read_only=True)
  # genre = SimpleGenreSerializer(read_only=True)
  images = BookImageSerializer(many=True, read_only=True)
  author = serializers.StringRelatedField()
  genre = serializers.StringRelatedField()

  class Meta:
    model = Book
    fields = ['id', 'title', 'author', 'genre', 'description', 'images']


class SimplestBookSerializer(serializers.ModelSerializer):
  """Serializer for the simplest Book"""

  class Meta:
    model = Book
    fields = ['id', 'title']


class BookEditionSerializer(serializers.ModelSerializer):
  """Serializer for BookEdition model"""
  # book = SimpleBookSerializer(read_only=True)
  book = MyBookSerializer(read_only=True)
  # publisher = PublisherSerializer(read_only=True)
  publisher = serializers.StringRelatedField()

  class Meta:
    model = BookEdition
    fields = ['id', 'book', 'booktype', 'isbn', 'unit_price',
              'price_with_tax', 'pages', 'bookformat',
              'publisher', 'publicationdate', 'stock', 'get_id_url']

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
              'publicationdate', 'get_id_url']
  
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
  bookedition = BookEditionSerializer()
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
  items_count = serializers.SerializerMethodField()

  def get_total_price(self, cart):
    return sum([item.quantity * item.bookedition.unit_price  for item in cart.items.all()])

  def get_items_count(self, cart):
    return sum(item.quantity for item in cart.items.all())
  
  class Meta:
    model = Cart
    fields = ['id', 'items', 'items_count', 'total_price']


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


class RemoveCartItemSerializer(serializers.ModelSerializer):
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
      self.instance = CartItem.objects.create(
        cart_id=cart_id, **self.validated_data
      )

    return self.instance

  class Meta:
    model = CartItem
    fields = ['id', 'bookedition_id', 'quantity']


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
  #bookedition = BookEditionSerializer(read_only=True)
  
  class Meta:
    model = OrderItem
    fields = [
              'bookedition',
              'quantity',
              # 'unit_price',
              'price',
            ]
    
class DisplayOrderItemSerializer(serializers.ModelSerializer):
  """Serializer for OrderItem in user account"""
  bookedition = BookEditionSerializer(read_only=True)
  
  class Meta:
    model = OrderItem
    fields = [
              'bookedition',
              'quantity',
              # 'unit_price',
              'price',
            ]


class DisplayOrderSerializer(serializers.ModelSerializer):
  """Serializer for Order in user account"""
  items = DisplayOrderItemSerializer(many=True)
  customer = serializers.StringRelatedField(read_only=True)
    
  class Meta:
    model = Order
    fields = [
              'id', 
              'customer',
              'fullname', 'phone', 'email',
              'shippingaddress', 'street',
              'zipcode', 'placed_at',
              'items', 'stripe_token','total_amount',
              'payment_status',
              ]   

class OrderSerializer(serializers.ModelSerializer):
  """Serializer for an Order"""
  items = OrderItemSerializer(many=True)

  class Meta:
    model = Order
    fields = [
              'id', 
              # 'customer',
              'fullname', 'phone', 'email',
              'shippingaddress', 'street',
              'zipcode',
              'items', 'stripe_token','total_amount',
              'payment_status',
              ]
  def create(self, validated_data):
    cart_items = validated_data.pop('items')
    order = Order.objects.create(**validated_data)
    
    for item_data in cart_items:
      OrderItem.objects.create(order=order, **item_data)

    return order


class UpdateOrderSerializer(serializers.ModelSerializer):
  """Serializer for updating an Order"""
  class Meta:
    model = Order
    fields = ['payment_status']


class CreateOrderSerializer(serializers.Serializer):
  """Serializer for creating an order"""

  def save(self, **kwargs):
    with transaction.atomic():
      # retrive the customer to place the order
      customer = Customer.objects.get(
        user_id=self.context['user_id']
      )
      # create the order
      # order = Order.objects.create(customer=customer, **validated_data)
      print(stripe.api_key)
  
      total_amount = sum(
        item.get('quantity') * item.get('bookedition').unit_price
        # item.get('price') for item in serializer.data['items']
          # for item in serializer.validated_data['items']
          for item in serializer.validated_data['items']
          )
      
      print("the total amount is", total_amount)
   
      try:
        print("about to charge")
        charge = stripe.Charge.create(
          amount=int(total_amount * 100),
          currency='USD',
          description='Charge from NabShop',
          source=serializer.validated_data['stripe_token'] # validated_data
        )
        print("charged")
    
        order = Order.objects.create(customer=customer, total_amount=total_amount, **validated_data)
        
        # retrieve the items in the cart 
        cart_items = validated_data.pop('items')
  
        # we create the order items for performance
        for item_data in cart_items:
          OrderItem.objects.create(order=order, **item_data)
        # delete the cart
        #Cart.objects.filter(pk=cart_id).delete()

        # make payment here

        # send a signal when an order is complete
        # send(): if a receiver failes to receive, other will not get notified
        order_created.send_robust(self.__class__, order=order)

        # update the payment status of the order
        return order
      except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AddressSerializer(serializers.ModelSerializer):
  """Serializer for Address model"""
  # customer = CustomerSerializer(read_only=True)
  customer_id = serializers.IntegerField(read_only=True)
  id = serializers.IntegerField(read_only=True)

  class Meta:
    model = Address
    fields = [ 'id', 'fullname', 'phone', 'country',
              'city', 'zipcode' ,'street', 'building',
              'shippingstatus', 'billingstatus', 'customer_id']

  def create(self, validated_data):
    customer_id = self.context['customer_id']
    return Address.objects.create(customer_id=customer_id,
                                 **validated_data)


# class PaymentMethodSerializer(serializers.ModelSerializer):
#   """Serializer for PaymentMethod model"""
#   class Meta:
#     model = PaymentMethod
#     fields = ['id', 'paymentmethodstatus', 'cardholder',
#               'country', 'paymenttype', 'provider', 'accountnumber',
#               "expirationdate"]
