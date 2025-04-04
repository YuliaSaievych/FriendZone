from django.urls import path
from .views import topic_list, topic_detail, add_comment, forum_feed

urlpatterns = [
    path('', topic_list, name='topic_list'),
    path('topic/<int:pk>/', topic_detail, name='topic_detail'),
    path('topic/<int:pk>/add_comment/', add_comment, name='add_comment'),
    path('forum-feed/', forum_feed, name='forum-feed'),
]