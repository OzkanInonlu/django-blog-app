from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["article", "comment_author", "comment_content", "comment_date"]
    list_display_links = ["comment_author", "comment_date"]

    class Meta:
        model = Comment 
        

#admin.site.register(Article)
# Equavilent to :
@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    #Admin sayfasında gösterilecek detaylar
    #Sırayla gösterilecek alanlar, bu sırayla gösterilecek 
    list_display = ["author", "title", "content", "created_date"]
    list_display_links = ["title", "created_date"]
    search_fields = ["title"]
    list_filter = ["title", "created_date"]

    class Meta:
        model = Article # ArticleAdmin ile Article'ı bağladık
        

