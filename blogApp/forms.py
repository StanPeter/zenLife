from django import forms
from .models import Post, Comment

class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)