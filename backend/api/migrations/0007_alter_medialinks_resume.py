# Generated by Django 4.1.7 on 2023-03-08 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_hello_alter_medialinks_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medialinks',
            name='resume',
            field=models.FileField(upload_to='images/resume'),
        ),
    ]
