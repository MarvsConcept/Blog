from django.urls import path

from . import views

urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("post/<slug:slug>", views.post_detail.as_view(), 
         name="post-detail"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later" )
]