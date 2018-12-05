from django.contrib import admin
from .models import *

class PostAdmin (admin.ModelAdmin):
    list_display = ["name",]

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)