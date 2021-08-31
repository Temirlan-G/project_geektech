# Generated by Django 3.2.6 on 2021-08-30 18:24

import distributor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0006_auto_20210822_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='ImageAboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=distributor.models.upload_to)),
                ('about_us', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributor.aboutus')),
            ],
            options={
                'verbose_name': 'Картинки о нас',
                'verbose_name_plural': 'Картинки о нас',
            },
        ),
    ]