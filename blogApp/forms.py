from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Sign up', 'Sign up', css_class='btn-primary'))
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
