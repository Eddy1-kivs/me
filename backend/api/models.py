from django.db import models

# Create your models here.

class Me(models.Model):
    name = models.CharField(max_length=100);
    title = models.CharField(max_length=155);
    description = models.TextField();
    image = models.ImageField(upload_to='images/profile');

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Name"

class About(models.Model):
    title = models.CharField(max_length=100);
    description = models.TextField();

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "About"


class Portfolio(models.Model):
    title = models.CharField(max_length=100);
    description = models.TextField();

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Portolio Title"


class PortfolioItems(models.Model):
    image = models.ImageField(upload_to='images/portfolio');
    title = models.CharField(max_length=100);
    description = models.TextField();
    link = models.URLField(blank=True, null=True);
    image1 = models.ImageField(upload_to='images/portfolio');
    image2 = models.ImageField(upload_to='images/portfolio');
    image3 = models.ImageField(upload_to='images/portfolio');
    image4 = models.ImageField(upload_to='images/portfolio');
    image5 = models.ImageField(upload_to='images/portfolio');
    image6 = models.ImageField(upload_to='images/portfolio');
    image7 = models.ImageField(upload_to='images/portfolio');

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Portfolio Items"


class Experience(models.Model):
    title = models.CharField(max_length=100);
    description = models.TextField();

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Experience Title"

class ExperienceItems(models.Model):
    image = models.ImageField(upload_to='images/experience');
    title = models.CharField(max_length=100);
    bottom_color = models.CharField(max_length=100, null=True);
    level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Experience Items"

class MediaLinks(models.Model):
    linkedin = models.URLField(blank=True, null=True)
    resume = models.FileField(upload_to='images/resume')
    github = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.linkedin
    
    class Meta:
        verbose_name_plural = "Media Links"


class Home(models.Model):
    greetings = models.CharField(max_length=100);
    name = models.CharField(max_length=100, null=True);

    def __str__(self):
        return self.greetings
    
    class Meta:
        verbose_name_plural = "Hello"


class Testimonials(models.Model):
    image = models.ImageField(upload_to='images/testimonials')
    name = models.CharField(max_length=100);
    role = models.CharField(max_length=100, blank=True, null=True);
    testimonial = models.TextField();

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Testimonials"


class ExperienceLevelTitle(models.Model):
    title = models.CharField(max_length=100);
    description = models.TextField();

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Experience Level Title"


class TestimonialTitle(models.Model):
    title = models.CharField(max_length=100);
    description = models.TextField();

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Testimonial Title"


class ContactTitle(models.Model):
    title = models.CharField(max_length=100);
    description = models.TextField();

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Contact Title"


class Projects(models.Model):
    WEBSITE = 'Website'
    APP = 'App'
    AI_ML = 'AI and Machine Learning'
    PROJECT_CATEGORIES = [
        (WEBSITE, 'Website'),
        (APP, 'App'),
        (AI_ML, 'AI and Machine Learning'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='images/projects')
    image1 = models.ImageField(upload_to='images/projects')
    image2 = models.ImageField(upload_to='images/projects', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/projects', blank=True, null=True)
    image4 = models.ImageField(upload_to='images/projects', blank=True, null=True)
    image5 = models.ImageField(upload_to='images/projects', blank=True, null=True)
    image6 = models.ImageField(upload_to='images/projects', blank=True, null=True)
    image7 = models.ImageField(upload_to='images/projects', blank=True, null=True)
    image8 = models.ImageField(upload_to='images/projects', blank=True, null=True)
    category = models.CharField(max_length=50, choices=PROJECT_CATEGORIES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Projects"
