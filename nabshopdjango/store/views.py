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

from .models import (Address, Author, Book, BookEdition, BookImage, Cart,
                     CartItem, Customer, Genre, Order, OrderItem, Publisher,
                     Review)
from .serializers import (AddCartItemSerializer, AuthorSerializer,
                          BookEditionSerializer, BookImageSerializer,
                          BookSerializer, CartItemSerializer, CartSerializer,
                          CreateOrderSerializer, CustomerReviewSerializer,
                          CustomerSerializer, GenreSerializer,
                          OrderItemSerializer, OrderSerializer,
                          PublisherSerializer, ReviewSerializer,
                          SimpleBookEditionSerializer, SimpleBookSerializer,
                          SimpleGenreSerializer, SimplestBookEditionSerializer,
                          SimplestBookSerializer, SimpleUserSerializer,
                          UpdateCartItemSerializer, UpdateOrderSerializer)

# class BookViewSet(ModelViewSet):
#   queryset = Book.objects.prefetch_related('images').all()
#   serializer_class = ProductSerializer
