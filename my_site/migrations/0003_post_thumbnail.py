# Generated by Django 4.0 on 2022-03-01 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0002_remove_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/images/construction.jpg', null=True, upload_to='images'),
        ),
    ]
