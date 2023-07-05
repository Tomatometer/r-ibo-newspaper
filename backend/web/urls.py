from django.urls import path
from web.views import *

app_name = "web"
urlpatterns = [
    path("", index, name="front-page"),
    # path("article/<str:articleID>", article_view, name="article"),
]
