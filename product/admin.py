from django.contrib import admin
from .models import (
    Category, Product, Tag
)

class ProductAdmin(admin.ModelAdmin):
	model = Product
	list_display = ('title', 'slug', 'image', 'description', 'price', 'created', 'active', 'category', 'stock')
	list_editable = ('active',)
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product, ProductAdmin)