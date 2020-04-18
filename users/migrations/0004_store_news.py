# Generated by Django 3.0.4 on 2020-04-17 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_store_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='store_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.CharField(blank=True, max_length=100)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.store')),
            ],
        ),
    ]
