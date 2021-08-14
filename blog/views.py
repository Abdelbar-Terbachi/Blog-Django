from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, DeleteView,UpdateView
from .models import Blog
from django.urls import reverse_lazy


# Create your views here.

class BlogListView(ListView):
    model=Blog
    template_name = 'home.html'
    context_object_name = 'blogs_list'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'post_detail.html'
    context_object_name = 'blog'

class BlogCreateView(CreateView):
    model = Blog
    template_name='new_post.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model=Blog
    template_name='post_edit.html'
    fields=['title','body']


class BlogDeleteView(DeleteView):
    model=Blog
    template_name='post_delete.html'
    success_url= reverse_lazy('home')




