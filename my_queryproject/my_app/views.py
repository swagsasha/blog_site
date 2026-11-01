from django.shortcuts import render
# Create your views here.
from .models import Post
from django.views.generic import ListView



class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_py = 5
    template =



