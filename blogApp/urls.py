from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


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
    path('post/<int:pk>/edit/', views.post_edit, name = 'post_edit'),

    #127.0.0.1:8000/draft
    #myApp.com/draft
    path('drafts/', views.post_draft, name = 'post_draft'),

    #127.0.0.1:8000/post/2/publish
    #myApp.com/post/2/publish
    path('post/<int:pk>/publish/', views.publish_draft, name='post_publish'),
 
    #127.0.0.1:8000/accounts/login
    #myApp.com/accounts/login
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

    #127.0.0.1:8000/accounts/logout
    #myApp.com/accounts/logout
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    #127.0.0.1:8000/accounts/logout
    #myApp.com/accounts/logout
    path('post/<int:pk>/comments/', views.add_comment, name='post_comment'),

]
    #path('accounts/', include('django.contrib.auth.urls')),

"""
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
"""