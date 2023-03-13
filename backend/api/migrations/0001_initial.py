# Generated by Django 4.1.7 on 2023-03-06 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Experiences/Skills',
            },
        ),
        migrations.CreateModel(
            name='ExperienceItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/experience')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Experience Items',
            },
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=155)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/profile')),
            ],
            options={
                'verbose_name_plural': 'Name',
            },
        ),
        migrations.CreateModel(
            name='PortfolioItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/portfolio')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
                ('image1', models.ImageField(upload_to='images/portfolio')),
                ('image2', models.ImageField(upload_to='images/portfolio')),
                ('image3', models.ImageField(upload_to='images/portfolio')),
                ('image4', models.ImageField(upload_to='images/portfolio')),
                ('image5', models.ImageField(upload_to='images/portfolio')),
                ('image6', models.ImageField(upload_to='images/portfolio')),
                ('image7', models.ImageField(upload_to='images/portfolio')),
            ],
            options={
                'verbose_name_plural': 'Portfolio Items',
            },
        ),
        migrations.CreateModel(
            name='Portolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Portolio',
            },
        ),
    ]
