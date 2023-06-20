from django.shortcuts import render
from web.models import *
# Create your views here.
def index(request):
    return render(request, "web/index.html")

def article_view(request, articleID):
    if request.method == "GET":
        return render(request, "web/article.html", {"article": Article.objects.get(article_id=articleID)})
