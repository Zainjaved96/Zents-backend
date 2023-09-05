# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination


class CreateProductView(APIView):
    @swagger_auto_schema(request_body=ProductSerializer)
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListProductsView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()

        # Apply pagination
        paginator = PageNumberPagination()
        paginated_products = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(paginated_products, many=True)

        return paginator.get_paginated_response(serializer.data)


class DeleteProductView(APIView):
    def delete(self, request, id, format=None):
        try:
            product = Product.objects.get(id=id)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


class ProductDetailView(APIView):
    def get(self, request, pk, format=None):
        try:
            product = Product.objects.get(id=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


class CategoryProductsView(APIView):
    def get(self, request, category_name, format=None):
        products = Product.objects.filter(category=category_name)

        # Apply pagination
        paginator = PageNumberPagination()
        paginated_products = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(paginated_products, many=True)

        return paginator.get_paginated_response(serializer.data)


class UpdateProductView(APIView):
    def put(self, request, pk, format=None):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
