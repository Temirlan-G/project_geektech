from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ConsultationQuestion(models.Model):
    class Meta:
        verbose_name = 'Вопрос консультации'
        verbose_name_plural = 'Вопросы консультации'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300, null=True)

