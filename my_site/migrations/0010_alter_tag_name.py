# Generated by Django 4.0 on 2022-03-12 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0009_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]