from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register('genres', views.GenreViewSet)
router.register('books', views.BookViewSet, basename='books')
router.register('bookeditions', views.BookEditionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')
# router.register("addresses", views.AddressViewSet, basename='addresses')

books_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
books_router.register('reviews', views.ReviewViewSet, basename='book-reviews')
books_router.register('images', views.BookImageViewSet, basename='book-images')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename="cart-items")

customers_router = routers.NestedDefaultRouter(router, 'customers', lookup='customer')
customers_router.register('addresses', views.AddressViewSet, basename='customer-addresses')

urlpatterns = router.urls + books_router.urls + carts_router.urls + customers_router.urls
