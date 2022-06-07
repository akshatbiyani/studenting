from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post

class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['blog_list']

    def location(self, item):
        return reverse(item)

class Article_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Post.objects.all()

    def location(self, obj):
        return f"/blog/{obj.slug}"

    def lastmod(self, obj): 
        return obj.date_added


class Topic_Sitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def location(self, obj):
        return f"/topic/{obj.topic}"

    def lastmod(self, obj): 
        return obj.date_added
