# Generated by Django 4.1.3 on 2022-11-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topartist',
            name='fans',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='topartist',
            name='img',
            field=models.ImageField(null=True, upload_to='media/top_artists/'),
        ),
    ]