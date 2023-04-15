from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post


class IndexView(generic.ListView):
    queryset = Post.objects.filter(status=True)
    context_object_name = "posts"
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"


class PostCreateView(generic.CreateView):
    model = Post
    template_name = "blog/post_create.html"
    success_url = reverse_lazy("index-page")
    fields = ["title", "content"]


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("index-page")
    fields = ["title", "content"]
class PostDeleteConfirimView(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete_confirm.html"
    success_url = reverse_lazy("index-page")
    fields = ["title", "content"]


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    success_url = reverse_lazy("index-page")
    fields = ["title", "content"]

class AboutView(generic.TemplateView):
    model = Post 
    template_name = "blog/about.html"
    
    

class ContactsView(generic.TemplateView):
    model = Post
    template_name = "blog/contacts.html"