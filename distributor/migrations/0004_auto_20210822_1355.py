# Generated by Django 3.2.6 on 2021-08-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0003_auto_20210822_1311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currentlegislation',
            options={'verbose_name': 'Действующее законодательство', 'verbose_name_plural': 'Действующее законодательство'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'Часто задаваемые вопросы', 'verbose_name_plural': 'Часто задаваемые вопросы'},
        ),
        migrations.AlterModelOptions(
            name='internationaldocuments',
            options={'verbose_name': 'Международные докумены', 'verbose_name_plural': 'Международные докумены'},
        ),
        migrations.AlterModelOptions(
            name='lawsnko',
            options={'verbose_name': 'Законодательство об НКО', 'verbose_name_plural': 'Законодательство об НКО '},
        ),
        migrations.AlterModelOptions(
            name='legalprojects',
            options={'verbose_name': 'Проекты нормативно-правовых актов', 'verbose_name_plural': 'Проекты нормативно-правовых актов'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='nkolibrary',
            options={'verbose_name': 'Библиотека об НКО', 'verbose_name_plural': 'Библиотека об НКО '},
        ),
        migrations.AlterField(
            model_name='lawsnko',
            name='intro',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
