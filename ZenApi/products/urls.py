from django.urls import path
from .views import CreateProductView, ListProductsView, DeleteProductView,\
    ProductDetailView, CategoryProductsView,UpdateProductView

urlpatterns = [
    path('create', CreateProductView.as_view(), name="create-product"),
    path('all', ListProductsView.as_view(), name="list-products"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/delete/<int:id>/', DeleteProductView.as_view(), name='delete-product'),
    path('product/<category_name>/', CategoryProductsView.as_view(), name='filter-category'),

]
