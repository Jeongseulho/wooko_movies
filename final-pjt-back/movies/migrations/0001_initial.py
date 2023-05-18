# Generated by Django 3.2.13 on 2023-05-18 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('popularity', models.FloatField(blank=True, null=True)),
                ('vote_average', models.FloatField(blank=True, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('poster_path', models.CharField(blank=True, max_length=200, null=True)),
                ('backdrop_path', models.CharField(blank=True, max_length=200, null=True)),
                ('genre_ids', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
    ]
