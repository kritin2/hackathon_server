# Generated by Django 3.0.4 on 2020-04-18 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_store_news_time_of_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store_news',
            name='time_of_post',
            field=models.DateTimeField(auto_now=True),
        ),
    ]