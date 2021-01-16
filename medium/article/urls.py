from django.urls import path

from .views import *


app_name = "articles"


urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('', index),
    path('articles/<int:pk>', ArticleView.as_view()),
]
