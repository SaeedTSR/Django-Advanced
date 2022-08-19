from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['author','title','category','created_date','status']
    
admin.site.register(Post,PostAdmin)
admin.site.register(Category)