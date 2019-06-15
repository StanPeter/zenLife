from django.urls import path
from . import views


urlpatterns = [
    # 127.0.0.1:8000
    # myApp.com 
    path('', views.post_list, name = 'post_list'),
    
    # 127.0.0.1:8000/post/1
    # myApp.com/post/1
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    #127.0.0.1:8000/post/new
    #myApp.com/post/new
    path('post/new/', views.post_new, name='post_new'),

    #127.0.0.1:8000/post/1/edit
    #myApp.com/post/1/edit
    path('post/<int:pk>/edit', views.post_edit, name = 'post_edit'),

    #127.0.0.1:8000/draft
    #myApp.com/draft
    path('drafts/', views.post_draft, name = 'post_draft'),

    #127.0.0.1:8000/post/2/publish
    #myApp.com/post/2/publish
    path('post/<int:pk>/publish', views.publish_draft, name='post_publish'),
 
]