from django.db import models

# Create your models here.

#Create Categories 
class NewRelease(models.Model):  #categories
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/categories/', null=True)

    def __str__(self):
        return self.name

class TopPlaylist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Proadcast(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TopArtist(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/top_artists/', null=True)
    fans = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name



class Song(models.Model):
    title= models.TextField()
    artist= models.ForeignKey(TopArtist, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='media/hindi_songs/', null=True)
    movie = models.CharField(max_length=100, null=True)
    tag = models.ForeignKey(NewRelease, on_delete=models.CASCADE, null=True)
    audio_file = models.FileField(blank=True,null=True, upload_to='media/songs/')
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)


    def __str__(self):
        return self.title