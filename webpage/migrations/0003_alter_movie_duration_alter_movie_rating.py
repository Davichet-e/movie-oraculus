# Generated by Django 4.0.3 on 2022-05-10 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_remove_movie_trending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.DurationField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
