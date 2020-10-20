from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=None, null=True)

# the publish date might differ from created
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True) #if post deleted the comments will be also deleted
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    approved = models.BooleanField(null=True, blank=True)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text


# class Sport(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name

# class Market(models.Model):
#     name = models.CharField(max_length=100)
#     sport = models.ForeignKey(Sport,related_name='markets', on_delete =models.CASCADE)
#     def __str__(self):
#         return self.name + ' | ' + self.sport.name

# class Selection(models.Model):
#     name = models.CharField(max_length=100)
#     odds = models.FloatField()
#     market = models.ForeignKey(Market,related_name='selections', on_delete =models.CASCADE)
#     def __str__(self):
#         return self.name

# class Match(models.Model):
#     name = models.CharField(max_length=100)
#     startTime = models.DateTimeField()
#     sport = models.ForeignKey(Sport, related_name='matches', on_delete =models.CASCADE)
#     market = models.ForeignKey(Market, related_name='matches', on_delete =models.CASCADE)
#     
#     class Meta:
#         ordering = ('startTime',)
#         verbose_name_plural = 'Matches'

#     def __str__(self):
#         return self.name