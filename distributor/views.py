from django.contrib.auth.models import User
from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework.response import Response

from .serializers import NewsListSerializer, NewsItemSerializer, NKOLibraryListSerializer, NKOLibraryItemSerializer, \
    LawsNKOSerializer, LawChaptersSerializer, FAQSerializer, AboutUsSerializer
from .models import News, ImageNews, NKOLibrary, LawsNKO, LawChapters, FAQ, AboutUs
from favorites.models import FavoriteNews
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        data = self.serializer_class(self.get_queryset(),
                                     many=True,
                                     context={'request': request}).data
        page = self.paginate_queryset(data)
        return self.get_paginated_response(page)


class NewsItemAPIView(generics.RetrieveAPIView):
    serializer_class = NewsItemSerializer
    queryset = News.objects.all()

    def post(self, request, *args, **kwargs):
        user = self.request.user
        news_id = self.kwargs.__getitem__('pk')
        if user.is_anonymous:
            return Response(
                data={
                    'message': 'user is anonymous'
                },
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        else:
            try:
                FavoriteNews.objects.get(news_id=news_id)
                FavoriteNews.objects.get(news_id=news_id).delete()
                return Response(data={'message': 'favorite deleted'})
            except FavoriteNews.DoesNotExist:
                favorite_add = FavoriteNews.objects.create(
                    user=user,
                    news_id=news_id
                )
                favorite_add.save()
                return Response(data={'message': 'favorite added'})


class NKOLibraryListAPIView(generics.ListAPIView):
    serializer_class = NKOLibraryListSerializer
    queryset = NKOLibrary.objects.all()


class NKOLibraryItemAPIView(generics.RetrieveAPIView):
    queryset = NKOLibrary.objects.all()
    serializer_class = NKOLibraryItemSerializer


class LawsNKOListAPIView(generics.ListAPIView):
    queryset = LawsNKO.objects.all()
    serializer_class = LawsNKOSerializer


class LawChaptersListAPIView(generics.ListAPIView):
    queryset = LawChapters.objects.all()
    serializer_class = LawChaptersSerializer


class FAQListAPIView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class AboutUsAPIView(generics.ListAPIView):
    serializer_class = AboutUsSerializer
    queryset = AboutUs.objects.all()