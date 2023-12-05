from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="post-page"),
    path("post/<slug:slug>", views.post_detail, name="post-detail")   
]