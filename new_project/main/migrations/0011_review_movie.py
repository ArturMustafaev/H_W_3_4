# Generated by Django 4.0.5 on 2022-06-21 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.movie'),
        ),
    ]
