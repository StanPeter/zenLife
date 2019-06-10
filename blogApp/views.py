from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import postForm
from .models import Post

# Create your views here.
def post_list(request):    #templates/blogApp/post_list.html but tempaltes is automatic
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blogApp/post_list.html', stuff_for_frontend)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = {'post': post}
    return render(request, 'blogApp/post_detail.html', stuff_for_frontend)
    
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
