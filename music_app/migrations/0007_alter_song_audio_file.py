# Generated by Django 4.2.11 on 2024-03-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0006_song_movie_song_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='media/songs/'),
        ),
    ]
