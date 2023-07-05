from web.views import *
from django.urls import path, include

app_name = "web"
urlpatterns = [
    path("", index, name="front-page"),
    path("article/<str:articleID>", article_view, name="article"),
]
