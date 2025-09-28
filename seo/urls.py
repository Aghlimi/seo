"""
URL configuration for seo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.shortcuts import render

def sitemap(request):
    return render(request, 'sitemap.xml', content_type='application/xml')
def sitemap_pages(request):
    return render(request, 'sitemap-pages.xml', content_type='application/xml')
def page(request, page_name='index.html'):
    return render(request, f'{page_name}')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:page_name>/', page, name='home'),
    path('', page, name='home'),
    path('robots.txt', lambda r: render(r, 'robots.txt', content_type='text/plain')),
    path('sitemap.xml', sitemap, name='sitemap'),
    path('sitemap-pages.xml', sitemap_pages, name='sitemap-pages')
]
    