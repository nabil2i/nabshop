from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action, permission_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin)
from rest_framework.permissions import (AllowAny, DjangoModelPermissions,
                                        DjangoModelPermissionsOrAnonReadOnly,
                                        IsAdminUser, IsAuthenticated)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from store.pagination import DefaultPagination
from store.permissions import (FullDjangoModelPermissions, IsAdminOrReadOnly,
                               ViewCustomerHistoryPermission)

from .filters import BookEditionFilter
from .models import (Address, Author, Book, BookEdition, BookImage, Cart,
                     CartItem, Customer, Genre, Order, OrderItem, Publisher,
                     Review)
from .serializers import (AddCartItemSerializer, AddressSerializer,
                          AuthorSerializer, BookEditionSerializer,
                          BookImageSerializer, BookSerializer,
                          CartItemSerializer, CartSerializer,
                          CreateOrderSerializer, 
                          CustomerSerializer,
                          GenreSerializer, OrderItemSerializer,
                          OrderSerializer, PublisherSerializer,
                          ReviewSerializer, SimpleBookEditionSerializer,
                          SimpleBookSerializer, SimpleGenreSerializer,
                          SimplestBookEditionSerializer,
                          SimplestBookSerializer, UpdateCartItemSerializer,
                          UpdateOrderSerializer,
                          DisplayOrderSerializer,
                          DisplayOrderItemSerializer)

import stripe
from django.conf import settings
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render



class GenreViewSet(ModelViewSet):
  queryset = Genre.objects.annotate(books_count=Count('books')).all()
  serializer_class = GenreSerializer
  permission_classes = [IsAdminOrReadOnly]

  def destroy(self, request, *args, **kwargs):
    if Book.objects.filter(book_id=kwargs['pk']).count() > 0:
      return Response(
        {
          'error': 'Genre cannot be deleted because it contains one or more books.'
        },
        status=status.HTTP_405_METHOD_NOT_ALLOWED
      )

    return super().destroy(request, *args, **kwargs)


class BookViewSet(ModelViewSet):
  queryset = Book.objects.prefetch_related('images', 'bookeditions').all()
  serializer_class = BookSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  search_fields = ['title']
  filterset_fields = ['genre__id']
  # pagination_class = DefaultPagination
  permission_classes = [IsAdminOrReadOnly]
  
  # search button in the navbar
 
  
  # ordering
  ordering_fields = ['created_at']

  # def get_queryset(self):
  #   queryset = Book.objects.prefetch_related('images', 'bookeditions').all()
  #   genre_id = self.request.query_params.get('genre_id')
  #   if genre_id is not None:
  #     queryset = queryset.filter(genre_id=genre_id)
  #   return queryset # add basename to the view in urls
    
  def get_serializer_context(self):
    # give the data posted by user to the serializer
    return {'request': self.request}

  def destroy(self, request, *args, **kwargs):
    if BookEdition.objects.filter(book_id=kwargs['pk']).count() > 0:
      return Response({
        'error': 'Book cannot be deleted because it is associated with an edition.'
        })
    return super().destroy(request, *args, **kwargs)


class BookEditionViewSet(ModelViewSet):
  def get_queryset(self):
    return BookEdition.objects.select_related('book').filter(book_id=self.kwargs['book_pk'])
  
  # queryset = BookEdition.objects.select_related('book').all()
  serializer_class = BookEditionSerializer
  # custom filtering
  filter_backends = [DjangoFilterBackend, SearchFilter]
  filterset_class = BookEditionFilter
  search_fields = ['book__title', 'book__description', 'book__genre__title']
  permission_classes = [IsAdminOrReadOnly]

  def get_serializer_context(self):
    return {'request': self.request}

  def destroy(self, request, *args, **kwargs):
    if OrderItem.objects.filter(bookedition_id=kwargs['pk']).count() > 0:
      return Response(
        {
          'error': 'Book Edition cannot be deleted because it is associated with an order item.'
        },
        status=status.HTTP_405_METHOD_NOT_ALLOWED
      )
    return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
  # queryset = Review.objects.all()
  serializer_class = ReviewSerializer

  def get_queryset(self):
    return Review.objects.filter(book_id=self.kwargs['book_pk'])

  def get_serializer_context(self):
    user = self.request.user
    customer_id = Customer.objects.only('id').get(user_id=user.id)
    return {
      'book_id' : self.kwargs['book_pk'],
      'customer_id': customer_id
      }


class CartViewSet(CreateModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
  queryset = Cart.objects.prefetch_related('items__bookedition').all()
  serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
  # serializer_class = CartItemSerializer
  # prevent put requests
  http_method_names = ['get', 'post', 'patch', 'delete']

  def get_serializer_class(self):
    if self.request.method == 'POST':
      return AddCartItemSerializer
    elif self.request.method == 'PATCH':
      return UpdateCartItemSerializer
    return CartItemSerializer

  # get the cart_id from the url and send it to
  # the serializer
  def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}

  def get_queryset(self):
    return CartItem.objects \
            .filter(cart_id=self.kwargs['cart_pk']) \
            .select_related('bookedition')


class CustomerViewSet(ModelViewSet
                      # RetrieveModelMixin,
                      # CreateModelMixin,
                      # UpdateModelMixin,
                      # GenericViewSet
                      ):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  permission_classes = [IsAdminUser]

  # any one can retrive a customer , but only admin can update
  # demo code for permissions
  # def get_permissions(self):
  #   if self.request.method == 'GET':
  #     return [AllowAny()]
  #   return [IsAuthenticated()]

  # custom model permission
  # @action(detail=True, permission_classes=[ViewCustomerHistoryPermission])
  # def history(self, request, pk):
  #   return Response('ok')
  

  @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
  def me(self, request):
    customer = Customer.objects.get(user_id=request.user.id)
    if request.method == 'GET':
      serializer = CustomerSerializer(customer)
      return Response(serializer.data)
    elif request.method == 'PUT':
      serializer = CustomerSerializer(customer, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)
############################################

# class OrderViewSet(ModelViewSet):
#   #permission_classes = [IsAuthenticated]
#   http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

#   def get_permissions(self):
#     if self.request.method in ['PATCH', 'DELETE']:
#       return [IsAdminUser()]
#     return [IsAuthenticated()]
  
#   # to get an order object instead of a cart_id we
#   # need to override the create() method
#   def create(self, request, *args, **kwargs):
#     serializer = CreateOrderSerializer(
#       data=request.data,
#       context={'user_id': self.request.user.id}
#       )
#     answer = serializer.is_valid()
#     print(answer)
#     print("serializer is: ", serializer)
#     print("initial data: ", serializer.initial_data)
#     print("validated_data is: ", serializer.validated_data)
    
#     order = serializer.save()
    
#     serializer = OrderSerializer(order)
#     return Response(serializer.data)
    

#   def get_serializer_class(self):
#     if self.request.method == 'POST':
#       return CreateOrderSerializer
#     elif self.request.method == 'PATCH':
#       return UpdateOrderSerializer
#     return OrderSerializer
  
#   def get_queryset(self):
#     user = self.request.user
#     if user.is_staff:
#       return Order.objects.all()
#     customer_id = Customer.objects.only('id').get(user_id=user.id)
#     return Order.objects.filter(customer_id=customer_id)

#   # def get_serializer_context(self):
#   #   return {'user_id': self.request.user.id}

class OrderViewSet(ModelViewSet):
  #permission_classes = [IsAuthenticated]
  http_method_names = ['get', 'patch', 'delete', 'head', 'options']

  def get_permissions(self):
    if self.request.method in ['PATCH', 'DELETE']:
      return [IsAdminUser()]
    return [IsAuthenticated()]

  def get_serializer_class(self):
    if self.request.method == 'PATCH':
      return UpdateOrderSerializer
    return DisplayOrderSerializer
  
  def get_queryset(self):
    user = self.request.user
    if user.is_staff:
      return Order.objects.all()
    customer = Customer.objects.only('id').get(user_id=user.id)
    return Order.objects.filter(customer=customer)

  def get_serializer_context(self):
    return {'user_id': self.request.user.id}


##########################################

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
  customer = Customer.objects.get(user_id=request.user.id)
  
  print("user id: ", request.user.id)
  print("customer: ", customer)
  
  serializer = OrderSerializer(data=request.data)
  answer = serializer.is_valid()
  
  print(answer)
  print("serializer is: ", serializer)
  print("initial data: ", serializer.initial_data)
  print("validated_data is: ", serializer.validated_data)
  

  stripe.api_key = settings.STRIPE_SECRET_KEY
  
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
    
    serializer.save(customer=customer, total_amount=total_amount)
    print("saved ok")
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  except Exception:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
class AddressViewSet(ModelViewSet):
  http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

  def get_permissions(self):
    if self.request.method in ['DELETE']:
      return [IsAdminUser()]
    return [IsAuthenticated()]

  def get_queryset(self):
    user = self.request.user
    user_id = user.id
    print(user_id)
    customer_id = Customer.objects.only('id').get(user_id=user_id).id
    print(customer_id)
    return Address.objects.filter(customer_id=customer_id)

  def get_serializer_context(self):
    user = self.request.user
    customer_id = Customer.objects.only('id').get(user_id=user.id).id
    return {'customer_id': customer_id}

  serializer_class = AddressSerializer
  
class BookImageViewSet(ModelViewSet):
  serializer_class = BookImageSerializer
  http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

  def get_permissions(self):
    if self.request.method in ['POST', 'PATCH', 'DELETE']:
      return [IsAdminUser()]
    return [AllowAny()]

  def get_serializer_context(self):
    return {'book_id': self.kwargs['book_pk']}

  def get_queryset(self):
    return BookImage.objects.filter(book_id=self.kwargs['book_pk'])
