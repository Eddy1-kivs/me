from django.urls import path, include
from rest_framework import routers
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('home/', views.home),
    path('me/', views.me),
    path('about/', views.about),
    path('portfolio/', views.portfolio),
    path('portfolio-item/', views.portfolio_item),
    path('portfolio-item/<str:pk>/', views.portfolio_items),
    path('experience/', views.experience),
    path('experience-item/', views.experience_item),
    path('media-links/', views.media_links),
    path('testimonials/', views.testimonials),
    path('testimonial-title/', views.testimonial_title),
    path('contact-title/', views.contact_title),
    path('experience-level-title/',  views.experience_level_title),
    path('projects/', views.projects),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
