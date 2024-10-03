from django.shortcuts import render, redirect
from .models import URL
from .forms import URLForm
import random
import string

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            short_url = generate_short_url()
            url = form.save(commit=False)
            url.short_url = short_url
            url.save()
            return redirect('shortener:link_list')
    else:
        form = URLForm()
    return render(request, 'shortener/home.html', {'form': form})

def link_list(request):
    urls = URL.objects.all()
    return render(request, 'shortener/link_list.html', {'urls': urls})

