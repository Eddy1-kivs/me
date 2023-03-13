# Generated by Django 4.1.7 on 2023-03-08 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_medialinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greetings', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Hello',
            },
        ),
        migrations.AlterModelOptions(
            name='medialinks',
            options={'verbose_name_plural': 'Media Links'},
        ),
    ]
