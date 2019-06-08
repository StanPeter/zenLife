from django.urls import path
from . import views


urlpatterns = [
    # 127.0.0.1:8000
    # myApp.com 
    path('', views.post_list, name = 'post_list'),
    
    # 127.0.0.1:8000/post/1
    # myApp.com/post/1
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
