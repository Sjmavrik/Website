from django.shortcuts import render
from .models import Art
from .forms import ArtForm


def news_home(request):
    news = Art.objects.all()
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    form = ArtForm()
    data = {
        'form': form
    }

    return render(request, 'news/create.html', data)
