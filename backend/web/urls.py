import web.views as wv
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name = "web"
urlpatterns = [
    path("", wv.index, name="front-page"),
    path("article/<uuid:articleID>", wv.article_view, name="article"),
    path("search/<str:searchKey>", wv.search_result, name="search"),
    path("author/<str:AuthorName>", wv.author_page, name="author"),
    path("comment/<str:articleID>", wv.comments, name="comment"),
    path("like/<str:articleID>", wv.like, name="like"),
    path("contact", wv.contact, name="contact"),
    path("about", wv.about, name="about"),
    path("posts", wv.posts, name="posts"),
    path("category/<slug:slug>/", wv.category_detail, name='category_detail'),
    path("issue/<slug:slug>/", wv.issue_detail, name='issue_detail')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)