from django.db import models

# Create your models here.

class Tweet(models.Model):
    content = models.TextField()
    user = models.ForeignKey("user.User", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tweet_image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.content
    
    
class Comment(models.Model):
    user = models.ForeignKey("user.User", on_delete = models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)