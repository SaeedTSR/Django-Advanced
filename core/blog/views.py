from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

def IndexFunc(request):
    return render(request ,'index.html')

class IndexClass(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context

class RedirectToMaktab(RedirectView):
    pattern_name = 'blog:class-index'

class PostListView(ListView):
    queryset = Post.objects.filter(status=1)
    context_object_name = 'posts'
    paginate_by = 2
    ordering = 'created_date'
    template_name = 'blog/post-list.html'

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=1)
    #     return posts
    
class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post-detail.html'
    
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post-create.html'
    success_url = '/blog/posts/'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post-create.html'
    success_url = '/blog/posts/'
    
class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post-delete.html'
    success_url = '/blog/posts/'