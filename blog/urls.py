from django.urls import path

from .views import BlogListView,blog_post


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('blog',blog_post ,name="blog_post")
]