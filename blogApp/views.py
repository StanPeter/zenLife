from django.shortcuts import render
from .models import Post
from django.utils import timezone


# Create your views here.
def post_list(request):    #templates/blogApp/post_list.html but tempaltes is automatic
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blogApp/post_list.html', stuff_for_frontend)
