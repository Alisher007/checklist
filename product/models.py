from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='product_images', default='default.jpg', blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, related_name='primary_products', blank=True, null=True, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
         return reverse("product:detail", kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product,self).save(*args, **kwargs)

    @property
    def in_stock(self):
        return self.stock > 0


def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


pre_save.connect(pre_save_product_receiver, sender=Product)









