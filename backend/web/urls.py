import web.views as wv
from django.urls import path

app_name = "web"
urlpatterns = [
    path("", wv.index, name="front-page"),
    path("article/<uuid:articleID>", wv.article_view, name="article"),
    path("search/<str:searchKey>", wv.search_result, name="search"),
    path("author/<str:AuthorName>", wv.author_page, name="author"),
    path("comment/<str:articleID>", wv.comments, name="comment"),
    path("like/<str:articleID>", wv.like, name="like"),
]
