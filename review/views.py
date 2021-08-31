from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer

from .models import Review


# Create your views here.


class UserReviewPost(APIView):
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        user = self.request.user
        if user.is_anonymous:
            return Response(
                data={
                    'message': 'log in or register'
                },
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        elif serializer.is_valid():
            try:
                review = Review.objects.create(
                    user=user,
                    review=serializer.validated_data['review'],
                    grade=serializer.validated_data['grade']
                )
                review.save()
                return Response(data={'message': 'review accepted'})
            except:
                return Response(data={'message': 'Вы уже оставляли отзыв'},
                                status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(data={'message': 'data error!',
                                  'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
