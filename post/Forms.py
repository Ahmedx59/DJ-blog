from django import forms
from .models import Post , Comment


class postform(forms.ModelForm):
    class Meta: 
        model = Post
        exclude = ['auth']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
