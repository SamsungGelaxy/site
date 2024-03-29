from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=("name", "emeil", "text")

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"id": "username", "class":"form-control", "placeholder": "Введть логін"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"id": "password", "class":"form-control", "placeholder": "Введть пароль"}))