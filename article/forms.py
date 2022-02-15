#from django import forms
from django.forms import ModelForm
from .models import *

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'article_image'] #author'ı eklemeye gerek yok çünkü sisteme giren kimse o olacak author