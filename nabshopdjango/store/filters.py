from django_filters.rest_framework import FilterSet
from .models import BookEdition

class BookEditionFilter(FilterSet):
  class Meta:
    model = BookEdition
    fields = {
      'unit_price': ['gt', 'lt']
    }