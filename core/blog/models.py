from django.db import models
from accounts.models import Profile

from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=255,null=True)
    
    def __str__(self):
        return self.name