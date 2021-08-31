"""figma_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from distributor import views
from registration import views as registration
from consultation import views as consultation
from review import views as review

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/news/', views.NewsListAPIView.as_view()),
    path('api/v1/news/<int:pk>/', views.NewsItemAPIView.as_view()),
    path('api/v1/library/', views.NKOLibraryListAPIView.as_view()),
    path('api/v1/library/<int:pk>', views.NKOLibraryItemAPIView.as_view()),
    path('api/v1/laws_nko/', views.LawsNKOListAPIView.as_view()),
    path('api/v1/nko_chapters/', views.LawChaptersListAPIView.as_view()),
    path('api/v1/FAQ/', views.FAQListAPIView.as_view()),
    path('api/v1/auth/otp/', registration.OTPView.as_view()),
    path('api/v1/auth/confirm/', registration.ConfirmOTPCodeView.as_view()),
    path('api/v1/question/', consultation.ConsultationQuestionPost.as_view()),
    path('api/v1/review/', review.UserReviewPost.as_view()),
    path('api/v1/about_us/', views.AboutUsAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
