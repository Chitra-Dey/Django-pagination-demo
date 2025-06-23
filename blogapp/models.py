from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100,default="Anonymous")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # add other fields as needed

    def __str__(self):
        return self.title