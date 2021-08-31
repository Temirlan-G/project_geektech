from django.shortcuts import render
from rest_framework.response import Response

from .models import ConsultationQuestion
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User


# Create your views here.
from .serializers import ConsultationQuestionSerializer


class ConsultationQuestionPost(APIView):
    def post(self, request):
        user = self.request.user
        if user.is_anonymous:
            return Response(
                data={
                    'message': 'error'
                },
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        else:
            question = ConsultationQuestion.objects.create(
                user=user,
                question=request.data['question']
            )
            question.save()
            return Response(data={'message': 'question accepted'})

    def get(self, request):
        user = self.request.user
        if user.is_anonymous:
            return Response(
                data={
                    'message': 'please register'
                },
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        else:
            questions = ConsultationQuestion.objects.filter(user=user)
            data = ConsultationQuestionSerializer(questions, many=True).data
            return Response(data=data)
