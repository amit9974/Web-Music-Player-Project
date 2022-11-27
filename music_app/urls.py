from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.home, name='home.html'),
    path('register/',views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.UserLogoutView, name='logout'),

    path('top_artist/', views.top_artist, name='top_artist'),
    path('new_release/', views.new_release, name='new_release'),
    path('hindi_songs/<int:id>/', views.hindi_songs, name='hindi_songs'),
    path('song/<int:id>/', views.playsongpage, name='song'),
    path('search/',views.search_song, name='search'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)