from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Post
from django.views.generic import ListView



class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 5
    template = "blog/post/list.html"




def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status="published", publish_year=year, publish_month=month, publish_day=day )
    return render(request, "blog/post/detail", {"post": post})

