# В forms.py
from .models import News, NewsImage, NewsVideo, NewsFile, Comment
from django import forms


class NewsImageForm(forms.ModelForm):
    class Meta:
        model = NewsImage
        fields = ['image']

class NewsVideoForm(forms.ModelForm):
    class Meta:
        model = NewsVideo
        fields = ['video']

class NewsFileForm(forms.ModelForm):
    class Meta:
        model = NewsFile
        fields = ['file']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'category', 'author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
