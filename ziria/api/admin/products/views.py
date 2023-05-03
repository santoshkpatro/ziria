from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.db.models import Count
from django.db import DatabaseError
from django.shortcuts import get_object_or_404

from ziria.mixins.store import StoreFetchMixin
from ziria.models.product import Product
from ziria.models.product_variant import ProductVariant
from .serializers import (
    ProductListSerializer,
    ProductListQuerySerializer,
    ProductDetailSerializer,
    ProductCreateSerializer,
    ProductUpdateSerializer,
)
from .pagination import ProductListPagination


class ProductViewSet(StoreFetchMixin, ProductListPagination, ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = ProductCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_product_data = serializer.validated_data
        try:
            new_product = Product.objects.create(
                **new_product_data, store=request.current_store
            )
            new_product_serializer = ProductDetailSerializer(new_product)
            return Response(
                data=new_product_serializer.data, status=status.HTTP_201_CREATED
            )
        except DatabaseError as e:
            return Response(
                data={"detail": "Error while creating new product"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def list(self, request, *args, **kwargs):
        # Instantiate a serializer for querying products based on query parameters
        query_serializer = ProductListQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)
        queries = query_serializer.validated_data

        # Retrieve products based on query parameters and current store,
        # annotate with the count of related product variants,
        # and order by creation date
        products = (
            Product.objects.filter(store=request.current_store, **queries)
            .annotate(variants_count=Count("product_variants"))
            .order_by("created_at")
        )

        # Paginate the products and serialize them using the ProductListSerializer
        page = self.paginate_queryset(products, request)
        serializers = ProductListSerializer(instance=page, many=True)

        # Return the paginated and serialized products as a Response object
        return self.get_paginated_response(data=serializers.data)

    def retrieve(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(store=request.current_store, id=kwargs["pk"])
            serializer = ProductDetailSerializer(instance=product)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(
                data={"detail": "Product with the given id not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def update(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(store=request.current_store, id=kwargs["pk"])

            update_serializer = ProductUpdateSerializer(data=request.data)
            update_serializer.is_valid(raise_exception=True)
            updated_data = update_serializer.validated_data

            try:
                for attr, value in updated_data.items():
                    setattr(product, attr, value)

                product.save()
            except DatabaseError as e:
                return Response(
                    data={"detail": "Unable to update data"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            serializer = ProductDetailSerializer(instance=product)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(
                data={"detail": "Product with the given id not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def destroy(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(store=request.current_store, id=kwargs["pk"])
            try:
                product.delete()
            except DatabaseError as e:
                return Response(
                    data={"detail": "Unable to update data"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            return Response(data={}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(
                data={"detail": "Product with the given id not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
