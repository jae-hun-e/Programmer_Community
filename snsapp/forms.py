from django import forms
from .models import Post, Comment, FreePost, FreeComment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['title', 'body']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class FreePostForm(forms.ModelForm):
    class Meta:
        model = FreePost
        fields = '__all__'

class FreeCommentForm(forms.ModelForm):
    class Meta:
        model = FreeComment
        fields = ['comment']