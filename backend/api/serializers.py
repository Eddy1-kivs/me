from rest_framework.serializers import ModelSerializer
from .models import *


class MeSerializer(ModelSerializer):
    class Meta:
        model = Me
        fields = ('__all__')


class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = ('__all__')


class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('__all__')


class PortfolioItemsSerializer(ModelSerializer):
    class Meta:
        model = PortfolioItems
        fields = ('__all__')


class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = ('__all__')


class ExperienceItemSerializer(ModelSerializer):
    class Meta:
        model = ExperienceItems
        fields = ('__all__')


class MediaLinksSerializer(ModelSerializer):
    class Meta:
        model = MediaLinks
        fields = ('__all__')


class HomeSerializer(ModelSerializer):
    class Meta:
        model = Home
        fields = ('__all__')


class TestimonialSerializer(ModelSerializer):
    class Meta:
        model = Testimonials
        fields = ('__all__')


class TestimonialTitleSerializer(ModelSerializer):
    class Meta:
        model = TestimonialTitle
        fields = ('__all__')


class ExperienceLevelTitleSerializer(ModelSerializer):
    class Meta:
        model = ExperienceLevelTitle
        fields = ('__all__')


class ContactTitleSerializer(ModelSerializer):
    class Meta:
        model = ContactTitle
        fields = ('__all__')


class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = ('__all__')