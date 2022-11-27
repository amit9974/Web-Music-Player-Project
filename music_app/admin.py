from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(NewRelease)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name',)

@admin.register(TopPlaylist)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name',)

@admin.register(TopArtist)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name',)

@admin.register(Proadcast)
class Admin(admin.ModelAdmin):
    '''Admin View for '''

    list_display = ('name',)

admin.site.register(Song)