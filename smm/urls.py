from django.urls import path
from . import views

urlpatterns = [
    path('postComment',views.postComment,name='postComment'),
    path('',views.blog,name='blog'),
    path('<str:slug>',views.post,name='post'),
]
