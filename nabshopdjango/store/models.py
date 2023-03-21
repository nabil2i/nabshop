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
  

class Genre(models.Model):
  """Model for a book genre"""
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

  def get_id_url(self):
    """Returns the url for the frontend"""
    # return f'/{self.slug}/'
    return f'/genres/{self.id}/'

  class Meta:
    ordering = ['title']

class Author(models.Model):
  """Model for an author"""
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  birth_date = models.DateField(null=True, blank=True)
  country = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self) -> str:
    return f'{self.first_name} {self.last_name}'

  class Meta:
    ordering = ['first_name', 'last_name']


class Book(models.Model):
  """Model for a book"""
  title = models.CharField(max_length=255)
  slug = models.SlugField()
  description = models.TextField(null=True, blank=True)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  genre = models.ForeignKey(Genre,
                            on_delete=models.PROTECT,
                            related_name='books')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return self.title

  def get_id_url(self):
    """Return the url for the frontend"""
    # return f'/{self.genre.slug}/{self.slug}/'
    return f'/{self.id}/'

  class Meta:
    ordering = ['title']


class BookImage(models.Model):
  """Model for images of a book"""
  book = models.ForeignKey(Book,
                           on_delete=models.CASCADE,
                           related_name="images")
  image = models.ImageField(upload_to='store/images',
                            validators=[validate_file_size],
                            blank=True,
                            null=True)
  # image = models.Image.Field(upload_to)
  thumbnail = models.ImageField(upload_to='store/thumbnails',
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

  def make_thumbnail(self, image, size=(200, 300)):
    """Makes a thumbnail based of an image"""
    img = Image.open(image)
    img.convert('RGB')
    img.thumbnail(size)

    thumb_io = BytesIO()
    img.save(thumb_io, 'JPEG', quality=85)

    thumbnail = File(thumb_io, name=image.name)

    return thumbnail


class Publisher(models.Model):
  """Model for a Publisher"""
  publisherhouse = models.CharField(max_length=255)
  city = models.CharField(max_length=255, null=True, blank=True)
  country = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self) -> str:
    return f'{self.publisherhouse}'

  class Meta:
    ordering = ['publisherhouse']


class BookEdition(models.Model):
  """Model for an inventory"""
  BOOKTYPE_EBOOK = 'Ebook'
  BOOKTYPE_PAPERBACK = 'Paperback'

  BOOKTYPE_CHOICES = [
        (BOOKTYPE_EBOOK, 'Ebook'),
        (BOOKTYPE_PAPERBACK, 'Paperback')
  ]
  slug = models.SlugField()
  booktype = models.CharField(max_length=10,
                              choices=BOOKTYPE_CHOICES,
                              default=BOOKTYPE_EBOOK)
  isbn = models.CharField(max_length=255)
  unit_price = models.DecimalField(max_digits=5,
                                   decimal_places=2,
                                   validators=[MinValueValidator(1)])
  pages = models.PositiveIntegerField(validators=[MinValueValidator(0)])
  bookformat = models.CharField(max_length=255)
  publisher = models.ForeignKey(Publisher,
                                on_delete=models.CASCADE,
                                related_name="bookeditions")
  publicationdate = models.DateField()
  stock = models.IntegerField(validators=[MinValueValidator(0)])
  book = models.ForeignKey(Book,
                           on_delete=models.CASCADE,
                           related_name='bookeditions')
  discounts = models.ManyToManyField('Discount', blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def get_id_url(self):
    """Returns the url for the frontend"""
    # return f'/{self.book.slug}/{self.slug}/'
    return f'/{self.id}/'

  def __str__(self) -> str:
    return f'{self.book.title}-{self.booktype}'

  class Meta:
    ordering = ['book__title']


class Customer(models.Model):
  """Model for a customer"""
  phone = models.CharField(max_length=255)
  birth_date = models.DateField(null=True, blank=True)
  user = models.OneToOneField(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f'{self.user.first_name} {self.user.last_name}'

  # add methods to get first name and last name at admin panel
  @admin.display(ordering='user__first_name')
  def first_name(self):
    return self.user.first_name

  @admin.display(ordering='user__last_name')
  def last_name(self):
    return self.user.last_name

  class Meta:
    ordering = ['user__first_name', 'user__last_name']
    permissions = [
      ('view_history', 'Can view history')
    ]


class Address(models.Model):
  """Model of an address of the customer"""
  ITEM_STATUS_YES = 'Y'
  ITEM_STATUS_NO = ('N')
    
  ITEM_STATUS_CHOICES = [
    (ITEM_STATUS_YES, 'Yes'),
    (ITEM_STATUS_NO, 'No'),
    ]
  fullname = models.CharField(max_length=255)
  phone = models.CharField(max_length=255)
  country = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  zipcode = models.SmallIntegerField()
  street = models.CharField(max_length=255)
  building = models.CharField(max_length=255)
  shippingstatus = models.CharField(
    max_length=1, choices=ITEM_STATUS_CHOICES,
    default=ITEM_STATUS_NO)
  billingstatus = models.CharField(
    max_length=1,
    choices=ITEM_STATUS_CHOICES,
    default=ITEM_STATUS_NO)
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
#   PAYMENTMETHOD_STATUS_YES = 'Y'
#   PAYMENTMETHOD_STATUS_NO = ('N')
    
#   PAYMENTMETHOD_STATUS_CHOICES = [
#     (PAYMENTMETHOD_STATUS_YES, 'Yes'),
#     (PAYMENTMETHOD_STATUS_NO, 'No'),
#     ]
#   paymentmethodstatus = models.CharField(
#     max_length=1, choices=PAYMENTMETHOD_STATUS_CHOICES,
#     default=PAYMENTMETHOD_STATUS_NO)
#   cardholder = models.CharField(max_length=255)
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


# if storing cart and cartitems in localstorage
# Cart and CartItem are not needed
class CartItem(models.Model):
  """Model of an item in a cart"""
  cart = models.ForeignKey(Cart,
                           on_delete=models.CASCADE,
                           related_name="items")
  bookedition = models.ForeignKey(BookEdition,
                                  on_delete=models.CASCADE)
  quantity = models.PositiveSmallIntegerField(
    validators=[MinValueValidator(1)])

  class Meta:
    # to have a single instance of a bookedition in the cart
    unique_together = [['cart', 'bookedition']]


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
  placed_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
  
  # new implementation adding these fields
  fullname = models.CharField(max_length=255)
  phone = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  # email = models.EmailField(max_length=255)
  shippingaddress = models.CharField(max_length=255)
  zipcode = models.CharField(max_length=255)
  street = models.CharField(max_length=255)

  
  total_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  stripe_token = models.CharField(max_length=255)


  class Meta:
    permissions = [
      ('cancel_order', 'Can cancel an order')
    ]
    ordering = ['-placed_at']
  
  def __str__(self):
    return self.fullname


class OrderItem(models.Model):
  """Model for an item in an order"""
  order = models.ForeignKey(Order,
                            on_delete=models.PROTECT,
                            related_name="items")
  bookedition = models.ForeignKey(BookEdition,
                                  on_delete=models.PROTECT,
                                  related_name="orderitems")
  quantity = models.PositiveSmallIntegerField(default=1)
  # unit_price = models.DecimalField(max_digits=8,
  #                                  decimal_places=2)
  price = models.DecimalField(max_digits=8,
                                  decimal_places=2)

  def __str__(self):
    return '%s' % self.id
