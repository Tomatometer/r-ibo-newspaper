import json
from uuid import *

# from django.core import serializers
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from web.models import *


# Create your views here.
def index(request: HttpRequest):
    return render(request, "web/new_layout.html")


def article_view(request: HttpRequest, articleID: UUID):
    if request.method == "GET":
        """
        return render(
            request,
            "web/new_layout.html",
            {
                "site": Article.objects.get(article_id=articleID),
                "posts": Article.objects.all()[0:5],
            }
        )
        """
        return JsonResponse(
            {"article": Article.objects.get(article_id=articleID).__dict__}, status=200
        )


def search_result(request: HttpRequest, searchKey: str):
    if request.method == "POST":
        result = []
        t = Article.objects.all()
        for x in t:
            if searchKey in x.title:
                result.append(x)
            else:
                continue
        return JsonResponse({"articles": result}, status=200)


def author_page(request: HttpRequest, AuthorName: str):
    if request.method == "POST":
        t = Article.objects.filter(author=AuthorName)
        author_info = Author.objects.get(name=AuthorName)
        return JsonResponse(
            {"authorInformation": author_info, "articles": t}, status=200
        )


def comments(request: HttpRequest, articleID: str):
    article = Article.objects.get(article_id=articleID)
    if request.method == "GET":
        comments = ArticleComment.objects.filter(article=article)
        return JsonResponse({"Comments": comments}, status=200)
    if request.method == "POST":
        try:
            new_comment = ArticleComment(
                commenter=request.user,
                article=article,
                comment_content=json.loads(request.body)["comment_content"],
            )
            new_comment.save()
            return JsonResponse({"Message": "Comment Created Sucessfully"}, status=200)
        except Exception:
            return JsonResponse({"Message": "Error creating comment"}, status=400)


def like(request: HttpRequest, articleID: str):
    us = request.user
    article = Article.objects.get(article_id=articleID)
    if request.method == "POST":
        try:
            like = LikedArticle.objects.get(article=article, liker=us)
            like.delete()
        except LikedArticle.DoesNotExist:
            like = LikedArticle(article=article, liker=us)
            like.save()
        return JsonResponse(
            {"Message": "like request recieved and processed"}, status=200
        )
