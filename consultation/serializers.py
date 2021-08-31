from rest_framework import serializers
from .models import ConsultationQuestion


class ConsultationQuestionSerializer(serializers.ModelSerializer):
        class Meta:
                model = ConsultationQuestion
                fields = 'id user question answer'.split()

