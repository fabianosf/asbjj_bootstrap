from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from accounts.models import UserProfile


''' 
class StaticViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return ['index', 'sobre', 'servicos', 'contato', 'login', 'logout', 'register']

    def location(self, item):
        return reverse(item)
'''

class ItemUserSitemap(Sitemap):
    def items(self):
        return UserProfile.objects.all()
    