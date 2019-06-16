from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import postForm, commentForm
from .models import Post, Comment

# Create your views here.
def post_list(request):    #templates/blogApp/post_list.html but tempaltes is automatic
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blogApp/post_list.html', stuff_for_frontend)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = {'post': post}
    return render(request, 'blogApp/post_detail.html', stuff_for_frontend)

@login_required    
def post_new(request):
    print(request.__dict__)

    if request.method == 'POST':
        form = postForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user    
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = postForm()
        stuff_for_frontend = {'form':form}
    return render(request, 'blogApp/post_new_edit.html', stuff_for_frontend)

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = postForm(request.POST, instance=post)

        if form.is_valid():
            print(request.method)

            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect ('post_detail', pk=post.pk)

    else:
        print(request.method)

        form = postForm(instance=post) #uses the current post and pass it to postForm()
        stuff_for_frontend = {'form':form, 'post':post}
    return render(request, 'blogApp/post_new_edit.html', stuff_for_frontend)

@login_required
def post_draft(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    stuff_for_frontend = {'posts' : posts}
    return render(request, 'blogApp/post_draft.html', stuff_for_frontend)

@login_required
def publish_draft(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = commentForm(request.POST)
        
        if form.is_valid:
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = commentForm()
        stuff_for_frontend = {'form':form}
        return render(request, 'blogApp/post_comment.html', stuff_for_frontend)

        