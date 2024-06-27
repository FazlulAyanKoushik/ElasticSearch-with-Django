from rest_framework import serializers

from .documents import ProductDocument
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price", "description", "image", "created_at", "updated_at")

class ProductDocumentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.FloatField()