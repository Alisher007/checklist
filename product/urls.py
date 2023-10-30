from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
     path('', views.HomeView.as_view(), name = 'home'),
     path('product/', views.ProductListView.as_view(), name = 'list'),
     path('create/', views.ProductCreateView.as_view(), name = 'create'),
     path('update/<pk>/', views.ProductUpdateView.as_view(), name = 'update'),
     path('detail/<slug>/', views.ProductDetailView.as_view(), name = 'detail'),
     path('tags/<product_id>/', views.TagListView.as_view(), name = 'tags'),
     path('tag-add/<tag_id>/<product_id>/', views.TagAddView.as_view(), name = 'tag-add'),
     path('tag-remove/<tag_id>/<product_id>/', views.TagRemoveView.as_view(), name = 'tag-remove'),
]
