# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, Comment, Reply

class PostAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'slug']
	class Meta:
		model = Post
  
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Reply)