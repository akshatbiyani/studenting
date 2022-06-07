from django.shortcuts import render
from django.views.generic import ListView   
# Create your views here.
from .models import Post

def main_page(request):
    posts = Post.objects.all()
    featured = Post.objects.filter(featured="RF")
    return render(request, 'blog/index.html', {
        "posts": posts, 
        "topics": list({i.topic for i in posts}),
        "count":4,
        "bigpost":Post.objects.filter(featured="LF")[0],
        "featured":sorted(featured,key=lambda x:x.feature_index)
        })



def blog_post(request,slug):
    post = Post.objects.filter(slug=slug)[0]
    return render(request,'blog/blog_post.html',{
        "post":post,
        "topic":post.topic,
        "posts":Post.objects.filter(topic=post.topic).exclude(slug=slug)
    })


def topic_page(request,topic):
    return render(request,'blog/topic-page.html',{
        "topic":topic,
        "posts":Post.objects.filter(topic=topic),
    })