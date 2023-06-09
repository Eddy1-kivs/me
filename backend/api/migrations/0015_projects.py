# Generated by Django 4.1.7 on 2023-03-12 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_contacttitle_experienceleveltitle_testimonialtitle_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images/projects')),
                ('image1', models.ImageField(upload_to='images/projects')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/projects')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/projects')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='images/projects')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='images/projects')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='images/projects')),
                ('image7', models.ImageField(blank=True, null=True, upload_to='images/projects')),
                ('image8', models.ImageField(blank=True, null=True, upload_to='images/projects')),
                ('category', models.CharField(choices=[('Website', 'Website'), ('App', 'App'), ('AI and Machine Learning', 'AI and Machine Learning')], max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
