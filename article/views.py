from django.shortcuts import redirect, render,HttpResponse, get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article, Comment


# Create your views here.
def index(requets):
    return render (requets, "index.html")

def about(requets):
    return render (requets, "about.html")
def dashboard(request):
    articles=Article.objects.filter(author=request.user)
    comments=Comment.objects.filter(comment_author=request)
    context={
        "articles":articles
    }
    
    return render (request, "dashboard.html", context)
def addArticle(request):
    form =ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request, "Meqale ugurla quruldu")
        return redirect("index")
    return render (request, "addarticle.html", {"form":form})
def detail(request, id):
    article=Article.objects.filter(id=id).first()
    article=get_object_or_404(Article, id=id)
    
    return render(request, "detail.html", {"article":article})
def updateArticle(request, id):

    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Məqalə uğurla yeniləndi")
        return redirect("article:dashboard")


    return render(request,"update.html",{"form":form})
def deleteArticle(request,id):
    article=get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request,"meqale ugurla silindi")
    return redirect("article:dashboard")
