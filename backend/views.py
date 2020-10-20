# #django imports
# from django.shortcuts import render, get_object_or_404, redirect
# from django.utils import timezone
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.contrib.auth import login
# from django.core.paginator import Paginator
# #customs
# from .forms import postForm, commentForm, userForm
# from .models import Post, Comment
# from .serializer import PostSerializer, CommentSerializer

# # Create your views here.
# def post_list(request):
#     all_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

#     paginator = Paginator(all_posts, 2)
#     page = request.GET.get('page')
#     posts = paginator.get_page(page)

#     page_range = []
#     for i in range(posts.number-3, posts.number+4):
#         if i >= 1 and i<= posts.paginator.num_pages:
#             page_range.append(i)
#     if len(page_range) < 2:
#         page_range = []

#     stuff_for_frontend = {'posts': posts, 'page_range':page_range}
#     return render(request, 'blogApp/post_list.html', stuff_for_frontend)

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     stuff_for_frontend = {'post': post}
#     return render(request, 'blogApp/post_detail.html', stuff_for_frontend)

# @login_required    
# def post_new(request):
#     print(request.__dict__)

#     if request.method == 'POST':
#         form = postForm(request.POST)
        
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user    
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)

#     else:
#         form = postForm()
#         stuff_for_frontend = {'form':form}
#     return render(request, 'blogApp/post_new_edit.html', stuff_for_frontend)

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)

#     if request.method == 'POST':
#         form = postForm(request.POST, instance=post)

#         if form.is_valid():
#             print(request.method)

#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect ('post_detail', pk=post.pk)

#     else:
#         print(request.method)

#         form = postForm(instance=post) #uses the current post and pass it to postForm()
#         stuff_for_frontend = {'form':form, 'post':post}
#     return render(request, 'blogApp/post_new_edit.html', stuff_for_frontend)

# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.delete()
#     return redirect('post_list')

# @login_required
# def post_draft(request):
#     posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
#     stuff_for_frontend = {'posts' : posts}
#     return render(request, 'blogApp/post_draft.html', stuff_for_frontend)

# @login_required
# def publish_draft(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.publish()
#     return redirect('post_detail', pk=pk)

# @login_required
# def add_comment(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         form = commentForm(request.POST)
        
#         if form.is_valid:
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = commentForm()
#         stuff_for_frontend = {'form':form}
#         return render(request, 'blogApp/post_comment.html', stuff_for_frontend)

# @login_required
# def delete_comment(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.delete()
#     return redirect('post_detail', pk=comment.post.pk)

# @login_required
# def approve_comment(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.approve()
#     return redirect('post_detail', pk=comment.post.pk)

# def singUp(request):
#     if request.method == 'POST':
#         form = userForm(request.POST)
#         if form.is_valid():
#             new_user = User.objects.create_user(**form.cleaned_data)
#             login(request, new_user)
#             return redirect('/')
#     else:
#         form = userForm()
#     return render(request, 'registration/sign_up.html', {'form':form})

# def articles(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#     stuff_for_frontend = {'posts': posts}
#     return render(request, 'blogApp/articles.html', stuff_for_frontend)

# def books(request):
#     return render(request, 'blogApp/books.html')

# def about(request):
#     return render(request, 'blogApp/about.html')

# def movies(request): 
#     return render(request, 'blogApp/movies.html')

# def terms_privacy(request):
#     return render(request, 'blogApp/terms_privacy.html')

# def thanks(request):
#     return render(request, 'blogApp/thanks.html')

# def summary(request):
#     return render(request, 'blogApp/summary.html')