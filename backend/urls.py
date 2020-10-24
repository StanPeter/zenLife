from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

from rest_framework import routers
from .api import PostViewSet, CommentViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, 'posts')
router.register(r'users', UserViewSet)

# router.register('comments/', CommentViewSet, 'comments')

# Routers provide an easy way of automatically determining the URL conf.

urlpatterns = [
    # path('forgot-password', ForgotPasswordFormView.as_view()),
    path(r'', include(router.urls)),
    # path('api-auth/', include())
]

# urlpatterns = [
#     #myApp.com/draft
#     path('drafts/', views.post_draft, name = 'post_draft'),

#     #myApp.com/post/2/publish
#     path('post/<int:pk>/publish/', views.publish_draft, name='post_publish'),

#     #myApp.com/post/2/comments/delete/

#     path('post/<int:pk>/comments/delete/', views.delete_comment, name='delete_comment'),

#     #myApp.com/post/2/comments/approve/
#     path('post/<int:pk>/comments/approve/', views.approve_comment, name='approve_comment'),

#     #myApp.com/articles
#     path('articles/', views.articles, name='articles'),

#     #myApp.com/books
#     path('books/', views.books, name='books'),

#     #myApp.com/about
#     path('about/', views.about, name='about'),

#     #myApp.com/movies
#     path('movies/', views.movies, name='movies'),

#     #myApp.com/terms_privacy
#     path('terms', views.terms_privacy, name='terms_privacy'),

#     #myApp.com/thanks
#     path('thanks', views.thanks, name='thanks'),

#     #myApp.com/summary
#     path('summary', views.summary, name='summary')

#     #path('accounts/', include('django.contrib.auth.urls')),
# ]

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
