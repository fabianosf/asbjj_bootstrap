from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return ['home', 'sobre', 'servicos', 'contato', 'login', 'logout', 'register']

    def location(self, item):
        return reverse(item)

    def get_urls(self, *args, **kwargs):
        urls = super().get_urls(*args, **kwargs)
        base_url = 'https://asbjj.com.br'
        return [url._replace(location=base_url + url.location) for url in urls]
