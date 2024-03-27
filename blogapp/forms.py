from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title' ,'content','header_image','snippet','category','author')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Snippet'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control', 'placeholder': 'Category'}),
            #'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'})
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id' : 'username', 'type':'hidden'})
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Snippet'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'})
        }