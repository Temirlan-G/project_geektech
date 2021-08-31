from django.db import models


# Create your models here.

def upload_to(instance, filename):
    return filename


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    full_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.title


class ImageNews(models.Model):
    class Meta:
        verbose_name = 'Картинки новости'
        verbose_name_plural = 'Картинки новостей'

    image = models.ImageField(upload_to=upload_to)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.news


class NKOLibrary(models.Model):
    class Meta:
        verbose_name = 'Библиотека об НКО'
        verbose_name_plural = 'Библиотека об НКО '

    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    publication = models.TextField()

    def __str__(self):
        return self.title


class LawsNKO(models.Model):
    class Meta:
        verbose_name = 'Законодательство об НКО'
        verbose_name_plural = 'Законодательство об НКО '

    intro = models.CharField(max_length=100, blank=True)
    chapters = models.CharField(max_length=100)

    def __str__(self):
        return self.chapters


class LawChapters(models.Model):
    class Meta:
        verbose_name = 'Разделы законодательств об НКО'
        verbose_name_plural = 'Разделы законодательств об НКО'

    nko_laws = models.ForeignKey(LawsNKO, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    full_description = models.TextField()

    def __str__(self):
        return self.title


class FAQ(models.Model):
    class Meta:
        verbose_name = 'Часто задаваемые вопросы'
        verbose_name_plural = 'Часто задаваемые вопросы'

    title = models.CharField(max_length=100)
    creating_description = models.CharField(max_length=100, null=True)
    creating = models.TextField()
    managing_description = models.CharField(max_length=100, null=True)
    managing = models.TextField()
    financing_description = models.CharField(max_length=100, null=True)
    financing = models.TextField()
    taxing_description = models.CharField(max_length=100, null=True)
    taxing = models.TextField()
    others_description = models.CharField(max_length=100, null=True)
    others = models.TextField()

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    title = models.CharField(max_length=100)
    description = models.TextField()
    # image = models.ImageField(upload_to=upload_to, null=True, blank=True)
    link = models.URLField()

    def __str__(self):
        return self.title


class ImageAboutUs(models.Model):
    class Meta:
        verbose_name = 'Картинки о нас'
        verbose_name_plural = 'Картинки о нас'

    image = models.ImageField(upload_to=upload_to)
    title = models.ForeignKey(AboutUs, on_delete=models.CASCADE)
