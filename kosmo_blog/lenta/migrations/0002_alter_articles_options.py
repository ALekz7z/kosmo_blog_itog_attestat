# Generated by Django 3.2 on 2022-11-26 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lenta', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]