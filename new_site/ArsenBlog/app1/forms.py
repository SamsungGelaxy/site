from django import forms
from .models import Comment, Post, PostPoint
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("title", "tag", "short_des", "img")

class PostPointForm(forms.ModelForm):
    class Meta:
        model=PostPoint
        fields=("header", "post_point_text", "post_img")


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=("name", "emeil", "text")

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"id": "username", "class":"form-control", "placeholder": "Введть логін"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"id": "password", "class":"form-control", "placeholder": "Введть пароль"}))