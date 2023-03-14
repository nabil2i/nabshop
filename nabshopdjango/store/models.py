from io import BytesIO
from uuid import uuid4

from django.conf import settings
from django.contrib import admin
from django.core.files import File
from django.core.validators import MinValueValidator
from django.db import models  # , File
from PIL import Image
from store.validators import validate_file_size


class Discount(models.Model):
  """Model for discounts"""
  DISCOUNT_STATUS_INACTIVE = 'I'
  DISCOUNT_STATUS_ACTIVE = 'A'

  DISCOUNT_STATUS_CHOICES = [
        (DISCOUNT_STATUS_INACTIVE, 'Inactive'),
        (DISCOUNT_STATUS_ACTIVE, 'Active')
  ]
  discount_status = models.CharField(max_length=1,
                                     choices=DISCOUNT_STATUS_CHOICES,
                                     default=DISCOUNT_STATUS_INACTIVE)
  title = models.CharField(max_length=255)
  description = models.TextField(null=True, blank=True)
  discount_percent = models.DecimalField(max_digits=3,
                                         decimal_places=2,
                                         validators=[MinValueValidator(0.01)])
  starts_at = models.DateTimeField()
  ends_at = models.DateTimeField()
  updated_at = models.DateTimeField(auto_now=True)
  

class Category(models.Model):
  """Model for a book category"""
  title = models.CharField(max_length=255)
  slug = models.SlugField()
  featured_book = models.ForeignKey('Book',
                                    on_delete=models.SET_NULL,
                                    related_name='+',
                                    blank=True,
                                    null=True)
  description = models.TextField(null=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return self.title

  def get_absolute_url():
    """Returns the url for the frontend"""
    return f'/{self.slug}/'

  class Meta:
    ordering = ['title']


class Book(models.Model):
  """Model for a book"""
  title = models.CharField(max_length=255)
  slug = models.SlugField()
  description = models.TextField(null=True, blank=True)
  author = models.CharField(max_length=255)
  bookcover = models.ImageField()
  category = models.ForeignKey(Category,
                               on_delete=models.PROTECT,
                               related_name='books')
  discounts = models.ManyToManyField('Discount', blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return self.title

  def get_absolute_url():
    """Return the url for the frontend"""
    return f'/{self.category.slug}/{self.slug}/'

  class Meta:
    ordering = ['-created_at']


class BookImage(models.Model):
  """Model for images of a book"""
  book = models.ForeignKey(Book,
                           on_delete=models.CASCADE,
                           related_name="images")
  image = models.ImageField(upload_to='store/uploads',
                            validators=[validate_file_size],
                            blank=True,
                            null=True)
  thumbnail = models.ImageField(upload_to='store/uploads',
                                blank=True,
                                null=True)
  updated_at = models.DateTimeField(auto_now=True)

  def get_image(self):
    """Retrieves an image"""
    if (self.image):
      return 'http://127.0.0.1:8000' + self.image.url
    return ''

  def get_thumbnail(self):
    """Retrieves a thumbnail"""
    if (self.thumbnail):
      return 'http://127.0.0.1:8000' + self.thumbnail.url
    else:
      if self.image:
        self.thumbnail = self.make_thumbnail(self.image)
        self.save()
        return 'http://127.0.0.1:8000' + self.thumbnail.url
      else:
        return ''

  def make_thumbnail(self, image, size=(300, 200)):
    """Makes a thumbnail based of an image"""
    img = Image.open(image)
    img.convert('RGB')
    impg.thumbnail(size)
    thumb_io = BytesIO()
    img.save(thumb_io, 'JPEG', quality=85)


class Inventory(models.Model):
  """Model for an inventory"""
  BOOKTYPE_EBOOK = 'E'
  BOOKTYPE_PAPERBACK = 'P'

  BOOKTYPE_CHOICES = [
        (BOOKTYPE_EBOOK, 'Ebook'),
        (BOOKTYPE_PAPERBACK, 'Paperback')
  ]
  booktype = models.CharField(max_length=1,
                              choices=BOOKTYPE_CHOICES,
                              default=BOOKTYPE_EBOOK)
  isbn = models.CharField(max_length=255)
  unit_price = models.DecimalField(max_digits=5,
                                   decimal_places=2,
                                   validators=[MinValueValidator(1)])
  pages = models.PositiveIntegerField(validators=[MinValueValidator(0)])
  bookformat = models.CharField(max_length=255)
  publicationdate = models.DateField()
  quantity = models.IntegerField(validators=[MinValueValidator(0)])
  book = models.ForeignKey(Book,
                           on_delete=models.CASCADE,
                           related_name='inventories')

  updated_at = models.DateTimeField(auto_now=True)


class Customer(models.Model):
  """Model for a customer"""
  phone = models.CharField(max_length=255)
  birth_date = models.DateField(null=True, blank=True)
  user = models.OneToOneField(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f'{self.user.first_name} {self.user.last_name}'

  # add methods to get first name and last name at admin panel
  @admin.display
  def first_name(self):
    return self.user.first_name

  @admin.display
  def last_name(self):
    return self.user.last_name

  class Meta:
    ordering = ['user__first_name', 'user__last_name']


class Address(models.Model):
  """Model of an address of the customer"""
  fullname = models.CharField(max_length=255)
  phone = models.CharField(max_length=255)
  country = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  zipcode = models.CharField(max_length=255)
  street = models.CharField(max_length=255)
  customer = models.ForeignKey(Customer,
                               on_delete=models.CASCADE,
                               related_name="addresses")
  updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
  """Model of a review made by a customer
  on a book
  """
  book = models.ForeignKey(Book,
                           on_delete=models.CASCADE,
                           related_name="reviews")
  customer = models.ForeignKey(Customer,
                               on_delete=models.PROTECT,
                               related_name="reviews")
  description = models.TextField()
  created_at = models.DateField(auto_now_add=True)


# class PaymentMethod(models.Model):
#   """Model of a payment method of the customer"""
#   name = models.CharField(max_length=255)
#   paymenttype = models.CharField(max_length=255)
#   provider = models.CharField(max_length=255)
#   accountnumber = models.PositiveIntegerField()
#   expirationdate = models.DateField()
#   customer = models.ForeignKey(Customer,
#                                on_delete=models.CASCADE,
#                                related_name="paymentmethods")
#   updated_at = models.DateTimeField(auto_now=True)


class Cart(models.Model):
  """Model of a cart"""
  id = models.UUIDField(primary_key=True,
                        default=uuid4)
  created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
  """Model of an item in a cart"""
  cart = models.ForeignKey(Cart,
                           on_delete=models.CASCADE,
                           related_name="items")
  book = models.ForeignKey(Book,
                           on_delete=models.CASCADE)
  quantity = models.PositiveSmallIntegerField(
    validators=[MinValueValidator(1)])

  class Meta:
    unique_together = [['cart', 'book']]


class Order(models.Model):
  """Model for an order"""
  PAYMENT_STATUS_PENDING = 'P'
  PAYMENT_STATUS_COMPLETE = 'C'
  PAYMENT_STATUS_FAILED = 'F'
  PAYMENT_STATUS_CHOICES = [
      (PAYMENT_STATUS_PENDING, 'Pending'),
      (PAYMENT_STATUS_COMPLETE, 'Complete'),
      (PAYMENT_STATUS_FAILED, 'Failed')
  ]

  payment_status = models.CharField(max_length=1,
                                    choices=PAYMENT_STATUS_CHOICES,
                                    default=PAYMENT_STATUS_PENDING)
  customer = models.ForeignKey(Customer,
                               on_delete=models.PROTECT,
                               related_name="orders")
  placed_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
  """Model for an item in an order"""
  order = models.ForeignKey(Order,
                            on_delete=models.PROTECT,
                            related_name="items")
  book = models.ForeignKey(Book,
                           on_delete=models.PROTECT,
                           related_name="orderitems")
  quantity = models.PositiveSmallIntegerField()
  unit_price = models.DecimalField(max_digits=5,
                                   decimal_places=2)
