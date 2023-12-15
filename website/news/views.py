from django.shortcuts import render, redirect
from .models import Art
from .forms import ArtForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Art.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewDatailView(DetailView):
    model = Art
    template_name = 'news/details_view.html'
    context_object_name = 'art'


class NewUpdatelView(UpdateView):
    model = Art
    template_name = 'news/create.html'

    form_class = ArtForm


class NewDeletelView(DeleteView):
    model = Art
    success_url = '/news/'
    template_name = 'news/delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма не верная'
    form = ArtForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)
