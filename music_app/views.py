from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.




def home(request):
    song = Song.objects.all()
    new_release = NewRelease.objects.all()
    top_artist = TopArtist.objects.all()
    top_playlist = TopPlaylist.objects.all()
    proadcast = Proadcast.objects.all()

    ctx ={
        'new_release':new_release,
        'top_artist':top_artist,
        'top_playlist':top_playlist,
        'proadcast':proadcast,
        'song':song,
  
    }

    return render(request, 'home.html', ctx)


def RegisterView(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')


        if password1 == password2:
            user = User.objects.create_user(username, email, password1)
            user.save()
            messages.success(request, 'User is created successfully')
            return redirect('/')
        else:
            messages.error(request, 'Password not match')
    ctx={
        'form':form,'title':'MUSIC | Register'
    }
            
    return render(request, 'accounts/register.html', ctx)


def LoginView(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('/')
        else:
            messages.error(request, 'Wrong Credentials')
    ctx={
        'form':form, 'title':'MUSIC | Login'
    }
    return render(request, 'accounts/login.html', ctx)

def UserLogoutView(request):
    logout(request)
    return redirect('/')


def top_artist(request):
    new_release = NewRelease.objects.all()
    top = TopArtist.objects.all()
    top_playlist = TopPlaylist.objects.all()
    proadcast = Proadcast.objects.all()

    ctx ={
        'new_release':new_release,
        'top':top,
        'top_playlist':top_playlist,
        'proadcast':proadcast,
    }
    return render(request, 'top_artist/top_artist.html', ctx)

def new_release(request):
    new_release = NewRelease.objects.all()
    top = TopArtist.objects.all()
    top_playlist = TopPlaylist.objects.all()
    proadcast = Proadcast.objects.all()

    ctx ={
        'new_release':new_release,
        'top':top,
        'top_playlist':top_playlist,
        'proadcast':proadcast,
    }
    return render(request, 'categories/categories.html', ctx)


def hindi_songs(request, id):
    song = Song.objects.filter(tag=id)
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    ctx={
        'new_release':new_release,
        'page_obj':page_obj,
        'song':song,
    }
    return render(request, 'categories/hindi/hindi.html', ctx )

@login_required(login_url='login')
def playsongpage(request, id):
    details = Song.objects.filter(id=id)
    ctx={
        'details':details,
    }
    return render(request, 'categories/hindi/details.html', ctx)



def search_song(request):
    ctx = {}
    query = request.GET.get('q')
    # print(query)
    ctx['song'] = Song.objects.filter(title__icontains=query)
    ctx['q'] = query
    return render(request, 'search.html',ctx)

