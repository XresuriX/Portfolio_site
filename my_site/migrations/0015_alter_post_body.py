# Generated by Django 4.0 on 2022-04-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0014_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
