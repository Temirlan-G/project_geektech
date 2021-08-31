from django.contrib import admin
from .models import *

# Register your models here.

# class NewsInLine(admin.StackedInline):
#     model = News
#     fields = 'title'.split()

admin.site.register(News)
admin.site.register(ImageNews)
admin.site.register(NKOLibrary)
admin.site.register(LawsNKO)
admin.site.register(LawChapters)
admin.site.register(FAQ)
admin.site.register(AboutUs)
admin.site.register(ImageAboutUs)
