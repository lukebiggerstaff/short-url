from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import Home, ShortUrl, redirect_to_url, store_and_return_shorturl

urlpatterns = [
    path('shorturl/<slug:url>/', ShortUrl.as_view(),name='short-url'),
    path('api/create/', store_and_return_shorturl),
    path('api', TemplateView.as_view(
        template_name='shortener/api.html'
    ), name='api'),
    path('<slug:url>', redirect_to_url),
    path('<slug:url>/', redirect_to_url),
    path('', Home.as_view(), name='home'),
]
