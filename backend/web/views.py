from django.http import HttpRequest
from django.shortcuts import render
from web.models import *


# Create your views here.
def index(request: HttpRequest):
    return render(request, "web/new_layout.html")


def article_view(request: HttpRequest, articleID: int):
    if request.method == "GET":
        return render(
            request,
            "web/new_layout.html",
            {
                "site": Article.objects.get(article_id=articleID),
                "posts": Article.objects.all()[0:5],
            },
        )
