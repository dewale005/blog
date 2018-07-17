# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import os
from django.db import models
from django.utils import timezone


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 99999999999999999)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "blog/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    text = models.TextField()
    User = models.ImageField(upload_to=upload_image_path, default='none')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/{slug}/".format(slug=self.slug)

class Comment(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE, related_name='comment_author')
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class Reply (models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE, related_name='reply_author')
    comment = models.ForeignKey('blog.Comment', on_delete=models.CASCADE, related_name='replys')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text