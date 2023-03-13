from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(['GET', 'POST'])
def me(request):
    me = Me.objects.all()
    serializer = MeSerializer(me, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def about(request):
    about = About.objects.all()
    serializer = AboutSerializer(about, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def portfolio(request):
    portfolio = Portfolio.objects.all()
    serializer = PortfolioSerializer(portfolio, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def portfolio_item(request):
    portfolioitem = PortfolioItems.objects.all()
    serializer = PortfolioItemsSerializer(portfolioitem, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def portfolio_items(request, pk):
    portfolioitem = PortfolioItems.objects.get(id=pk)
    serializer = PortfolioItemsSerializer(portfolioitem, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def experience(request):
    experience = Experience.objects.all()
    serializer = ExperienceSerializer(experience, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def experience_item(request):
    experienceitem = ExperienceItems.objects.all()
    serializer = ExperienceItemSerializer(experienceitem, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def experience_items(request, pk):
    experienceitem = ExperienceItems.objects.get(id=pk)
    serializer = ExperienceItemSerializer(experienceitem, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def media_links(request):
    media_links = MediaLinks.objects.all()
    serializer = MediaLinksSerializer(media_links, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def home(request):
    home = Home.objects.all()
    serializer = HomeSerializer(home, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def testimonials(request):
    testimonials = Testimonials.objects.all()
    serializer = TestimonialSerializer(testimonials, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def testimonial_title(request):
    testimonial_title = TestimonialTitle.objects.all()
    serializer = TestimonialTitleSerializer(testimonial_title, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def experience_level_title(request):
    experience_level_title = ExperienceLevelTitle.objects.all()
    serializer = ExperienceLevelTitleSerializer(experience_level_title, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def contact_title(request):
    contact_title = ContactTitle.objects.all()
    serializer = ContactTitleSerializer(contact_title, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def projects(request):
    projects = Projects.objects.all()
    serializer = ProjectsSerializer(projects, many=True)
    return Response(serializer.data)
