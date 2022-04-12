# Generated by Django 4.0 on 2022-03-02 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0003_post_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='my_site.Tag'),
        ),
    ]
