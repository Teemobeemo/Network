from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import Post

# Form to make a new post
class NewPostForm(forms.ModelForm):
    content = forms.CharField(max_length=500,label=False,widget=forms.Textarea(attrs={'placeholder': 'Content'}))

    class Meta:
        model = Post
        fields=[
            'content'
        ]