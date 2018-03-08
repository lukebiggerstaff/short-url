from django.contrib import admin
from django.urls import path
from .views import Home, ShortUrl, redirect_to_url, store_and_return_shorturl

urlpatterns = [
    path('shorturl/<slug:url>/', ShortUrl.as_view(),name='short-url'),
    path('api/create/', store_and_return_shorturl),
    path('<slug:url>', redirect_to_url),
    path('<slug:url>/', redirect_to_url),
    path('', Home.as_view()),
]
