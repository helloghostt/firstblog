from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

def get_default_user():
    return User.objects.filter(is_superuser=True).first()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)