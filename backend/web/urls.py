from django.urls import path
import web.views as wv

app_name = "web"
urlpatterns = [
    path("", wv.index, name="front-page"),
    path("search/<str:searchKey>", wv.search_result, name="search"),
    path("author/<str:AuthorName>", wv.author_page, name="article"),
    path("comment/<str:articleID>", wv.comments, name="comment"),
    path("like/<str:articleID>", wv.like, name="like")
    
]
