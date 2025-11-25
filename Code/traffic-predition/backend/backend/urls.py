"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),  # ✅ Django Admin Panel
    path("api/", include("api.urls", namespace="api")),  # ✅ Include API routes
]

# ✅ Serve media files in development (for images, uploads, etc.)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
