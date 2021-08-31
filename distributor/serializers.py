from rest_framework import serializers

from favorites.models import FavoriteNews
from .models import News, ImageNews, NKOLibrary, LawsNKO, LawChapters, FAQ, AboutUs, ImageAboutUs


class NewsListSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = 'id title short_description created_at image is_favorite'.split()

    def get_is_favorite(self, news):
        user = self.context['request'].user
        if user.is_anonymous:
            return False
        return bool(FavoriteNews.objects.filter(user=user, news_id=news.id).count() > 0)


class NewsItemSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = 'id title full_description link images'.split()

    def get_images(self, news):
        images = ImageNews.objects.filter(news=news)
        return [i.image.url for i in images]


class NKOLibraryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NKOLibrary
        fields = 'id title'.split()


class NKOLibraryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NKOLibrary
        fields = 'id title created_at publication'.split()


class LawsNKOSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawsNKO
        fields = 'id chapters'.split()


class LawChaptersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawChapters
        fields = 'id nko_laws title short_description'.split()


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = 'id title creating_description creating managing_description managing ' \
                 'financing_description financing taxing_description taxing others_description others'.split()


class AboutUsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = AboutUs
        fields = 'id title description link images'.split()

    def get_images(self, about_us_id):
        images = ImageAboutUs.objects.filter(title_id=about_us_id)
        return [i.image.url for i in images]