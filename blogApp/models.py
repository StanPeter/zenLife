from django.db import models
from django.utils import timezone

# Create your models here.
# that's how you create tables 
# whenever changed execute python manage.py makemigrations

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=None)

# the publish date might differ from created

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blogApp.Post', on_delete=models.CASCADE, related_name='comments') #if post deleted the comments will be also deleted
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text
