from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    review = models.CharField(max_length=255, blank=True, null=True)
    grade = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
