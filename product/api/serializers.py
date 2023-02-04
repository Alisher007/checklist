from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from core.models import (
    Tax, Category, Payment, Customer, Product, OrderItem, Order
)

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = (
            'id',
            'name',
            'percent',
            'active'
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'id',
            'amount',
            'timestamp'
        )


class CustomerDetailSerializer(serializers.ModelSerializer):
    order = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = (
            'id',
            'name',
            'lastname',
            'phone',
            'email',
            'order'
        )

    def get_order(self, obj):
        return OrderSerializer(obj.order).data


class ProductSerializer(serializers.ModelSerializer):
    secondary_categories = serializers.SerializerMethodField()
    primary_category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'slug',
            'barcode',
            'image',
            'description',
            'price',
            'created',
            'updated',
            'active',
            'stock',
            'quantity',
            'primary_category',
            'secondary_categories'
        )

    def get_primary_category(self, obj):
        return CategorySerializer(obj.primary_category).data

    def get_secondary_categories(self, obj):
        return CategorySerializer(obj.secondary_categories.all(), many=True).data


class OrderItemDetailSerializer(serializers.ModelSerializer):
    order = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = (
            'id',
            'product',
            'quantity',
            'price',
            'discount'
        )

    def get_order(self, obj):
        return OrderSerializer(obj.order).data

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'created',
            'updated',
            'ordered'
        )






