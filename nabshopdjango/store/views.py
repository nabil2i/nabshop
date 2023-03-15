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
from .serializers import (AddCartItemSerializer, AuthorSerializer,
                          BookEditionSerializer, BookImageSerializer,
                          BookSerializer, CartItemSerializer, CartSerializer,
                          CreateOrderSerializer, CustomerSerializer,
                          GenreSerializer, OrderItemSerializer,
                          OrderSerializer, PublisherSerializer,
                          ReviewSerializer, SimpleBookEditionSerializer,
                          SimpleBookSerializer, SimpleGenreSerializer,
                          SimplestBookEditionSerializer,
                          SimplestBookSerializer, UpdateCartItemSerializer,
                          UpdateOrderSerializer)


class GenreViewSet(ModelViewSet):
  queryset = Genre.objects.annotate(books_count=Count('books')).all()
  serializer_class = GenreSerializer
  # permission_classes = [IsAdminOrReadOnly]

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
  filterset_fields = ['genre_id']
  pagination_class = DefaultPagination
  # permission_classes = [IsAdminOrReadOnly]
  
  # search button in the navbar
  search_fields = ['title', 'description', 'genre__title']
  
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
  queryset = BookEdition.objects.select_related('book').all()
  serializer_class = BookEditionSerializer
  # custom filtering
  filter_backends = [DjangoFilterBackend, SearchFilter]
  filterset_class = BookEditionFilter
  search_fields = ['book__title', 'book__description', 'book__genre__title']

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
    return {
      'book_id' : self.kwargs['book_pk'],
      # modify the customer_id to be the connected customer_id
      # request.user.customer_id
      'customer_id': 1
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
