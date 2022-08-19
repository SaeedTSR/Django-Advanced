from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'blog'

urlpatterns = [
    path('func',view=views.IndexFunc,name='func-index'),
    path('class',view=views.IndexClass.as_view(),name='class-index'),
    path('redirect',view=views.RedirectToMaktab.as_view(),name='redirect'),
    path('posts/',view=views.PostListView.as_view(),name='post-list'),
    path('posts/<int:pk>/',view=views.PostDetailView.as_view(),name='post-detail'),
    path('posts/create/',view=views.PostCreateView.as_view(),name='post-create'),
    path('posts/<int:pk>/edit/',view=views.PostEditView.as_view(),name='post-edit'),
    path('posts/<int:pk>/delete/',view=views.PostDeleteView.as_view(),name='post-delete'),
]
