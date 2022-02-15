from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Article(models.Model):
    #baska bir tablo ile ilişkilendirdik (auth.User TABLE)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar") 
    
    title = models.CharField(max_length=50, null=True, verbose_name="Başlık")
    
    content = RichTextField(verbose_name="İçerik") # TextArea
    
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi") #Anlık tarihi alacak
    
    article_image = models.FileField(blank=True, null=True, verbose_name="Makale Fotoğrafı")
    
    class Meta:
        ordering = ["-created_date"]
        
    def __str__(self): #admin panelinde ne gözüksün?
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Article", related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="Comment Writer")
    comment_content = models.TextField(max_length=200, verbose_name="Comment")
    comment_date = models.DateField(auto_now_add=True, verbose_name="Comment Date")

    class Meta:
        ordering = ["-comment_date"]

    def __str__(self): #admin panelinde ne gözüksün?
        return self.comment_content