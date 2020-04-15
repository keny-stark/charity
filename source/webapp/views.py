from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from webapp.models import News


class IndexView(ListView):
    context_object_name = 'news'
    model = News
    template_name = 'index.html'