from rest_framework import serializers

from ziria.models.product import Product


class ProductListQuerySerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Product.Status.choices, required=False)
    search = serializers.CharField(required=False)

class ProductListSerializer(serializers.ModelSerializer):
    variants_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "slug",
            "status",
            "created_at",
            "updated_at",
            "variants_count",
        )

    def get_variants_count(self, obj):
        return obj.variants_count


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "status",
            "created_at",
            "updated_at",
        )


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "status",
            "created_at",
            "updated_at",
        )


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "title",
            "slug",
            "description",
            "status"
        )