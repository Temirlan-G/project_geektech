# Generated by Django 3.2.6 on 2021-08-26 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultationquestion',
            name='answer',
            field=models.CharField(max_length=300, null=True),
        ),
    ]