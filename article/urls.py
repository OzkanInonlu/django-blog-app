from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from blog import settings

app_name = "article"

urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('article/<int:id>', views.detail, name = "detail"),
    path('addArticle/', views.addArticle, name = "addArticle"),
    path('updateArticle/<int:id>', views.updateArticle, name = "updateArticle"),
    path('deleteArticle/<int:id>', views.deleteArticle, name = "deleteArticle"),
    path('', views.showArticles, name="articles"),
    path('comment/<int:id>', views.makeComment, name="comment"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


