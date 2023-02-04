import django_filters
from .models import Product, Tag

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='title')
    description = django_filters.CharFilter(lookup_expr='icontains', label='description')
    price = django_filters.RangeFilter(label='price')

    class Meta:
        model = Product
        fields = ['title','description','category','active' ,'price']

class TagFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='name')

    class Meta:
        model = Tag
        fields = ['name']

