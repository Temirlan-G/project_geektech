# Generated by Django 3.2.6 on 2021-08-20 17:21

import distributor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=200)),
                ('full_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to=distributor.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='ImageNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=distributor.models.upload_to)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributor.news')),
            ],
        ),
    ]
