from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.Serializer):
    review = serializers.CharField(max_length=255)
    grade = serializers.IntegerField(max_value=5, min_value=1)