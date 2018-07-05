# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from .models import Post


class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'blog/post_list.html'

    model = Post
    paginate_by = 50  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PostDetailSlugView(DetailView):
    queryset = Post.objects.all()
    template_name = 'blog/post_detail.html'

class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'blog/post_detail.html'

    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['now'] = timezone.now()
        return context    

    