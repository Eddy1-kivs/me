# Generated by Django 4.1.7 on 2023-03-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_portolio_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='experienceitems',
            name='bottom_color',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='experienceitems',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
