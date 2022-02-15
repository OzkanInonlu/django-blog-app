from django.shortcuts import get_object_or_404, render, HttpResponse, redirect, reverse
from .models import *
from .forms import *
from django.contrib import messages
import time
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
import datetime
# Create your views here.

def index(request):
    Article_List = Article.objects.all()
    return render(request, 'index.html', {"Article_List": Article_List})
    #return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def detail(request, id):
    #article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)

    #Comments
    Comment_List = Comment.objects.filter(article=article).order_by("-comment_date") 

    #OR
    #related_name = "comments"
    #Comment_List = article.comments.all()

    return render(request, 'detail.html',{"article": article, "Comment_List": Comment_List})

@login_required(login_url = "user:login") #eğer login olmadıysa, login url'ye git
def dashboard(request):
    #sadece giriş yapan kişiye ait olanları alalım
    Article_List = Article.objects.filter(author=request.user).order_by("-created_date") 
    username = request.user.username
    username = username.upper()
    return render(request, 'dashboard.html', {"username": username, "Article_List": Article_List})

@login_required(login_url = "user:login")
def addArticle(request):
#form.save(commit=False) diyerek kaydedebilin ModelForm oldugundan, alttakilerine gerek kalmaz

#form = ArticleForm(request.POST or None, request.FILES or None)
#article objesi oluşturuldu, ve article.save() yaptı. Ama User verilmedi, hata verecek.
#o yüzden commit = False deyerek save'i yapmasını engelle, biz yapacayık.

#article.author = request.user dememiz lazım

#article.save()
#-------------------------------------
#article = form.save(commit = False)

#article.author = request.user

#article.save()

#form = ArticleForm(request.POST or None, request.FILES or None)

    form = ArticleForm()

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            
            title = form.cleaned_data['title']

            content = form.cleaned_data['content']

            article_img = form.cleaned_data['article_image']

            Article.objects.create(author = request.user, title=title, content=content, 
            article_image=article_img)

            messages.success(request, "Your article is saved")
            return redirect("article:dashboard")

    return render(request, 'addArticle.html', {"form":form})
       
@login_required(login_url = "user:login")
def updateArticle(request, id):

# Creating a form to change an existing article / UPDATE
# article = Article.objects.get(pk=1)
# form = ArticleForm(instance=article)
# Every ModelForm also has a save() method.
# A subclass of ModelForm can accept an existing model instance as the keyword argument 'instance';
# if this is supplied, save() will update that instance. If it’s not supplied, 
# save() will create a new instance of the specified model:

    article = get_object_or_404(Article, id=id)

    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)

    if form.is_valid():
        
        title = form.cleaned_data['title']

        content = form.cleaned_data['content']

        article_img = form.cleaned_data['article_image']

        Article.objects.filter(id=id).update(title = title, content = content, article_image = article_img)

        messages.success(request, "Your article is modified")
        return redirect("article:dashboard")

    return render(request, 'updateArticle.html', {"form":form})


@login_required(login_url = "user:login")
#NetStaff.objects.filter(uuid=remove_staff_uuid).delete()
def deleteArticle(request, id):
    #article = get_object_or_404(Article, id=id).delete()
    Article.objects.filter(id=id).first().delete()

    messages.info(request, "Your article is deleted")
    
    return redirect("article:dashboard")


def showArticles(request):
    keyword = request.POST.get('keyword')

    if keyword:
        #keyword'u içeren article'lar
        Article_List = Article.objects.filter(title__contains=keyword)
        return render(request, 'articles.html', {"Article_List":Article_List})

    Article_List = Article.objects.all()

    return render(request, 'articles.html', {"Article_List":Article_List})

def makeComment(request, id):
    
    article = Article.objects.filter(id=id).first()

    if request.method == 'POST':
        comment_author = request.POST.get('comment_author')
        comment_content = request.POST.get('comment_content')

        Comment.objects.create(article=article, comment_author=comment_author, comment_content=comment_content)

    #dinamik url '<int:id>' olduğundan
    return redirect(reverse("article:detail", kwargs={"id":id}))



    