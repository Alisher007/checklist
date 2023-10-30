from django.shortcuts import get_object_or_404, reverse, redirect, render
from django.conf import settings
from django.views import generic
from .models import Product, Category, Tag
from .filters import ProductFilter, TagFilter
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(generic.TemplateView):
    template_name = 'home.html'

############ Product to list all products
class ProductListView(generic.ListView):
    template_name = 'product/product_list.html'
    queryset = Product.objects.all().order_by('-updated')
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context

class ProductDetailView(generic.DetailView):
    template_name = 'product/product_detail.html'
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

############ Product create view
class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ProductForm
    template_name = 'product/product_create.html'

    def form_valid(self, form):
        new_item = form.save(commit=False)
        new_item.save()
        return super().form_valid(form)

############ Product update view
class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = ProductForm
    template_name = 'product/product_update.html'

    def get_queryset(self):
        return Product.objects.filter(pk=self.kwargs["pk"])

    def form_valid(self, form):
        new_item = form.save(commit=False)
        new_item.save()
        return super().form_valid(form)


############ Tag to list all tags
class TagListView(LoginRequiredMixin, generic.ListView):
    template_name = 'product/cat_list.html'
    queryset = Tag.objects.all()
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = TagFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs["product_id"]
        if product_id:
            context['product_id'] = product_id
        context['form'] = self.filterset.form
        return context

class TagAddView(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        tag_id = self.kwargs["tag_id"]
        product_id = self.kwargs["product_id"]
        tag = get_object_or_404(Tag, id=tag_id)
        product = Product.objects.filter(pk=product_id).first()
        product.tag.add(tag)
        product.save()
        messages.info(self.request,'The Tag has been added/updated')
        return redirect("product:detail", slug=product.slug)

class TagRemoveView(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        tag_id = self.kwargs["tag_id"]
        tag = get_object_or_404(Tag, id=tag_id)
        product_id = self.kwargs["product_id"]
        product = Product.objects.filter(pk=product_id).first()
        product.tag.remove(tag)
        product.save()
        messages.info(self.request,'The Tag has been removed')
        return redirect("product:detail", slug=product.slug)
























