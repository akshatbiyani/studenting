from django.shortcuts import render
from django.views.generic import ListView   
# Create your views here.
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'


def blog_post(request):
    slug = request.url.split('/')[-1]
    return render(request,'blog/blog_post.html',{
        "post":Post.object.filter(slug=slug)
    })


def topic_page(request):
    posts = Post.objects.filter(topic="test")