from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    Ingredients = forms.CharField(label='Ingredients',widget=forms.Textarea(attrs={
        'rows': '3',
        'placeholder': 'Enter Ingredients...'
    }))
    Recipe = forms.CharField(label='Recipe', widget=forms.Textarea(attrs={
        'rows': '3',
        'placeholder': 'Enter the Recipe...'
    }))

    Title = forms.CharField(label='Title', max_length=50,)

    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['Title','Ingredients', 'Recipe','image']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='',widget=forms.Textarea(attrs={
        'rows': '2',
        'placeholder': 'Enter Comment'
    }))
   

    class Meta:
        model = Comment
        fields = ['comment']